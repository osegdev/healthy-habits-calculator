from app.interfaces.console_menu import show_menu
from app.use_cases.create_habit import create_habit

habits = []


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


def main():
    print("Bienvenido a la Calculadora de Hábitos Saludables")
    while True:
        choice = show_menu()
        if choice == "1":
            handle_create_habit()
        elif choice == "2":
            print("👉 Registrar entrada diaria (en construcción)")
        elif choice == "3":
            print("👉 Historial (en construcción)")
        elif choice == "4":
            print("👋 Saliendo del programa.")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
