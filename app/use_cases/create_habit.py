from app.domain.habit import Habit


def create_habit(name: str, unit: str, goal: float, type_: str) -> Habit:
    if not name or not unit or not type_:
        raise ValueError("Todos los campos deben estar completos.")
    if goal <= 0:
        raise ValueError("La meta debe ser un numero positivo.")
    return Habit(name=name, unit=unit, goal=goal, type_=type_)
