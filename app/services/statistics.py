from collections import defaultdict
from statistics import mean
from typing import List
from app.domain.record import Record
from app.domain.habit import Habit
from datetime import timedelta
from datetime import date
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

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

def weekly_summary(records: List[Record], habits: List[Habit]) -> str:
    today = date.today()
    last_week = today - timedelta(days=7)
    recent_records = [r for r in records if last_week <= r.record_date <= today]

    if not recent_records:
        return "📭 No hay registros en los últimos 7 días."

    summary = defaultdict(list)
    for r in recent_records:
        summary[r.habit_name].append(r)

    result = "\n📆 Resumen semanal:\n"
    for habit_name, habit_records in summary.items():
        habit = next((h for h in habits if h.name == habit_name), None)
        if not habit:
            continue
        total = sum(r.value for r in habit_records)
        promedio = total / len(habit_records)
        cumplimiento = (promedio / habit.goal) * 100
        result += (
            f"- {habit_name}: registros = {len(habit_records)}, "
            f"promedio = {promedio:.2f} {habit.unit}, "
            f"cumplimiento promedio = {cumplimiento:.0f}%\n"
        )
    return result

console = Console()

def plot_weekly_ascii(records: List[Record], habits: List[Habit]):
    today = date.today()
    last_week = today - timedelta(days=7)

    filtered = [r for r in records if last_week <= r.record_date <= today]
    if not filtered:
        console.print("[bold red]No hay registros en la última semana[/]")
        return

    summary = defaultdict(float)
    for r in filtered:
        summary[r.habit_name] += r.value

    table = Table(title="Resumen semanal")
    table.add_column("Hábito")
    table.add_column("Total acumulado")

    for habit, total in summary.items():
        table.add_row(habit, f"{total:.2f}")

    console.print(table)