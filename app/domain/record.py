from dataclasses import dataclass
from datetime import date


@dataclass
class Record:
    habit_name: str
    value: float
    record_date: date
