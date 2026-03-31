from datetime import datetime
from pawpal_system import Task, Pet


def test_task_completion():
    task = Task(
        description="Feed pet",
        scheduled_time=datetime.now(),
        priority=1,
        frequency="daily"
    )

    task.mark_complete()

    assert task.completed == True


def test_add_task_to_pet():
    pet = Pet("Buddy", "Dog", 3)

    task = Task(
        description="Walk dog",
        scheduled_time=datetime.now(),
        priority=2,
        frequency="daily"
    )

    pet.add_task(task)

    assert len(pet.tasks) == 1