from datetime import date, datetime

from app.interfaces.console_menu import show_menu
from app.interfaces.command_router import execute_command
from app.services.statistics import summarize_records
from app.services.storage import (
    load_habits,
    load_records,
    save_habits,
    save_records,
    export_records_to_csv,
    backup_data,
)
from app.use_cases.create_habit import create_habit
from app.use_cases.register_entry import register_entry

habits = load_habits()
records = load_records()


def handle_create_habit():
    print("\n👉 Registrar nuevo hábito")
    name = input("Nombre del hábito: ")
    unit = input("Unidad de medida (ej: litros, pasos): ")
    goal = float(input("Meta diaria: "))
    type_ = input("Tipo de hábito (agua, pasos, calorías, etc.): ")
    try:
        habit = create_habit(name, unit, goal, type_)
        habits.append(habit)
        save_habits(habits)
        print(f"✅ Hábito '{habit.name}' registrado exitosamente.")
    except ValueError as e:
        print(f"❌ Error: {e}")


def handle_register_entry():
    print("\n👉 Registrar entrada diaria")
    if not habits:
        print("⚠️ No hay hábitos registrados. Primero registre uno.")
        return
    for i, habit in enumerate(habits):
        print(f"{i + 1}. {habit.name} ({habit.unit})")

    index = int(input("Seleccione el hábito (número): ")) - 1
    if index < 0 or index >= len(habits):
        print("❌ Hábito inválido.")
        return

    try:
        value = float(input(f"Ingrese cantidad de '{habits[index].name}': "))
        date_str = input("Fecha (YYYY-MM-DD) [Enter para hoy]: ").strip()
        entry_date = (
            datetime.strptime(date_str, "%Y-%m-%d").date()
            if date_str
            else date.today()
        )
        record = register_entry(habits[index].name, value, entry_date)
        records.append(record)
        save_records(records)
        print(
            f"✅ Entrada registrada para {record.habit_name} "
            f"el {record.record_date}"
        )
    except ValueError as e:
        print(f"❌ Error: {e}")


def handle_view_history():
    print("\n📖 Historial de entradas")
    if not records:
        print("📭 No hay entradas registradas.")
        return

    for record in records:
        print(f"- {record.record_date} | {record.habit_name}: {record.value}")

    print(summarize_records(records))


def handle_export_and_backup():
    if not records:
        print("📭 No hay registros para exportar.")
        return
    export_records_to_csv(records)
    backup_data()
    print("✅ Historial exportado y respaldo creado.")


def main():
    print("🎯 Bienvenido a la Calculadora de Hábitos Saludables 🎯")

    handlers = {
        "1": handle_create_habit,
        "2": handle_register_entry,
        "3": handle_view_history,
        "4": lambda: print("📦 Guardando datos... ¡Hasta luego!"),
        "5": handle_export_and_backup,
    }

    while True:
        choice = show_menu()
        if choice == "4":
            handlers["4"]()
            break
        execute_command(choice, handlers)


if __name__ == "__main__":
    main()
