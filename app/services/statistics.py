from collections import defaultdict
from statistics import mean
from typing import List
from app.domain.record import Record
from app.domain.habit import Habit

def summarize_records(records: List[Record]) -> str:
    if not records:
        return "📭 No hay registros disponibles."

    summary = defaultdict(list)
    for r in records:
        summary[r.habit_name].append(r.value)

    result = "\n📊 Resumen de registros:\n"
    for habit, values in summary.items():
        total = sum(values)
        promedio = mean(values)
        result += f"- {habit}: total = {total}, promedio = {promedio:.2f}\n"
    return result

def calculate_progress(record: Record, habits: List[Habit]) -> str:
    habit = next((h for h in habits if h.name == record.habit_name), None)
    if not habit:
        return "Meta no encontrada"
    percent = (record.value / habit.goal) * 100
    status = "✅ Cumplido" if percent >= 100 else "📈 En progreso"
    return f"{percent:.0f}% ({status})"