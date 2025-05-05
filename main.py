from datetime import date, datetime

from app.interfaces.console_menu import show_menu
from app.use_cases.create_habit import create_habit
from app.use_cases.register_entry import register_entry

habits = []
records = []


def handle_create_habit():
    print("\n👉 Registrar nuevo hábito")
    name = input("Nombre del hábito: ")
    unit = input("Unidad de medida (ej: litros, pasos): ")
    goal = float(input("Meta diaria: "))
    type_ = input("Tipo de hábito (agua, pasos, calorías, etc.): ")
    try:
        habit = create_habit(name, unit, goal, type_)
        habits.append(habit)
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
        print(
            f"✅ Entrada registrada para {record.habit_name} "
            f"el {record.record_date}"
        )
    except ValueError as e:
        print(f"❌ Error: {e}")


def main():
    print("Bienvenido a la Calculadora de Hábitos Saludables")
    while True:
        choice = show_menu()
        if choice == "1":
            handle_create_habit()
        elif choice == "2":
            handle_register_entry()
        elif choice == "3":
            print("👉 Historial (en construcción)")
        elif choice == "4":
            print("👋 Saliendo del programa.")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
