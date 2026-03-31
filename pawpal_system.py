from dataclasses import dataclass, field
from typing import List
from datetime import datetime


# Task 
@dataclass
class Task:
    description: str
    scheduled_time: datetime
    priority: int
    frequency: str
    completed: bool = False

    def mark_complete(self):
        self.completed = True

    def display_task(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.description} at {self.scheduled_time} ({status})"


# Pet 
@dataclass
class Pet:
    name: str
    type: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


# Owner 
class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


# Scheduler 
class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self):
        return self.owner.get_all_tasks()

    def get_tasks_for_today(self):
        today = datetime.now().date()
        return [
            task for task in self.get_all_tasks()
            if task.scheduled_time.date() == today
        ]

    def get_pending_tasks(self):
        return [
            task for task in self.get_all_tasks()
            if not task.completed
        ]

    def generate_daily_plan(self):
        tasks = self.get_tasks_for_today()
        # sort by priority (higher first) and time
        tasks.sort(key=lambda t: (-t.priority, t.scheduled_time))
        return tasks