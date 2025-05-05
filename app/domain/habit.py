from dataclasses import dataclass


@dataclass
class Habit:
    name: str
    unit: str
    goal: float
    type_: str
