from datetime import datetime
from typing import List


class Schedule:
    def __init__(self, day: str, entry_time: datetime, departure_time: datetime):
        self.day = day
        self.entry_time = entry_time
        self.departure_time = departure_time


class Employee:
    def __init__(self, name: str, weekly_schedule: List[Schedule]):
        self.name = name
        self.weekly_schedule = weekly_schedule
