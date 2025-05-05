from datetime import date

from app.domain.record import Record


def register_entry(habit_name: str, value: float, entry_date: date) -> Record:
    if not habit_name or value < 0:
        raise ValueError(
            "Nombre del hábito requerido y valor no puede ser negativo."
        )
    return Record(habit_name=habit_name, value=value, record_date=entry_date)
