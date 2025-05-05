from collections import defaultdict
from statistics import mean
from typing import List
from app.domain.record import Record

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