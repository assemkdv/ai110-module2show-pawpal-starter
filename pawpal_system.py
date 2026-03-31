from dataclasses import dataclass, field
from typing import List
from datetime import datetime


# Pet
@dataclass
class Pet:
    name: str
    type: str
    age: int
    notes: str = ""

    def update_pet_info(self):
        pass

    def display_pet_info(self):
        pass


# Task
@dataclass
class Task:
    task_name: str
    duration: float
    priority: int
    scheduled_time: datetime

    def update_task(self):
        pass

    def mark_complete(self):
        pass

    def display_task(self):
        pass


# Schedule 
class Schedule:
    def __init__(self):
        self.tasks: List[Task] = []
        self.date = None
        self.available_time = 0.0

    def add_task(self, task: Task):
        pass

    def generate_daily_plan(self):
        pass

    def get_tasks_for_today(self):
        pass


# User
class User:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet: Pet):
        pass

    def view_pets(self):
        pass