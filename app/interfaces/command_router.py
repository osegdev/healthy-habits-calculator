def execute_command(choice, handlers):
    if choice in handlers:
        handlers[choice]()
    else:
        print("❌ Opción inválida. Intente de nuevo.")