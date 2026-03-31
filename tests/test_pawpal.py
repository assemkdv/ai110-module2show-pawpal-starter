from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def test_sorting_tasks_by_time():
    owner = Owner("Test")
    pet = Pet("Buddy", "Dog", 3)
    owner.add_pet(pet)

    t1 = Task("Late Task", datetime.now().replace(hour=18), 1, "daily")
    t2 = Task("Early Task", datetime.now().replace(hour=9), 1, "daily")

    pet.add_task(t1)
    pet.add_task(t2)

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time(scheduler.get_all_tasks())

    assert sorted_tasks[0].description == "Early Task"
    assert sorted_tasks[1].description == "Late Task"


def test_recurring_task_creates_new_task():
    owner = Owner("Test")
    pet = Pet("Buddy", "Dog", 3)
    owner.add_pet(pet)

    task = Task(
        "Feed Dog",
        datetime.now(),
        1,
        "daily"
    )

    pet.add_task(task)

    new_task = task.mark_complete()

    assert task.completed is True
    assert new_task is not None
    assert new_task.scheduled_time.date() == (task.scheduled_time + timedelta(days=1)).date()


def test_conflict_detection():
    owner = Owner("Test")
    pet = Pet("Buddy", "Dog", 3)
    owner.add_pet(pet)

    same_time = datetime.now().replace(hour=10, minute=0)

    t1 = Task("Task 1", same_time, 1, "daily")
    t2 = Task("Task 2", same_time, 1, "daily")

    pet.add_task(t1)
    pet.add_task(t2)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1