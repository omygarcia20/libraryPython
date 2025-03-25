from users.user import create_user, consult_users, update_user, delete_user

def main_menu():
    # Muestra el menú principal y permite al usuario seleccionar un área del sistema.

    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Gestión de Usuarios.")
        print("2. Gestión de Libros.")
        print("3. Gestión de Préstamos.")
        print("4. Salir")
        
        case = input("Seleccione una opción: ")
        
        if case == "1":
            user_menu()
        elif case == "2":
            print("Gestión de Libros.")
        elif case == "3":
            print("Gestión de Préstamos.")
        elif case == "4":
            print("Saliste del sistema.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def user_menu():
    
    # Muestra el menú de gestión de usuarios.

    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Crear Usuario")
        print("2. Consultar Usuarios")
        print("3. Modificar Usuario")
        print("4. Eliminar Usuario")
        print("5. Volver al Menú Principal")
        
        case = input("Seleccione una opción: ")
        
        if case == "1":
            # Crear usuario
            name = input("Ingrese el nombre: ")
            lastName = input("Ingrese el apellido: ")
            phone = input("Ingrese el teléfono: ")
            email = input("Ingrese el correo electrónico: ")
            identity = input("Ingrese el número de identificación: ")
            create_user(name, lastName, phone, email, identity)
        elif case == "2":
            # Consultar usuarios
            consult_users()
        elif case == "3":
            # Modificar usuario
            email = input("Ingrese el correo del usuario a modificar: ")
            name = input("Nuevo nombre (dejar en blanco para no modificar): ")
            lastName = input("Nuevo apellido (dejar en blanco para no modificar): ")
            phone = input("Nuevo teléfono (dejar en blanco para no modificar): ")
            new_email = input("Nuevo correo (dejar en blanco para no modificar): ")
            identity = input("Nueva identificación (dejar en blanco para no modificar): ")
            update_user(email, name or None, lastName or None, phone or None, new_email or None, identity or None)
        elif case == "4":
            # Eliminar usuario
            email = input("Ingrese el correo del usuario a eliminar: ")
            delete_user(email)
        elif case == "5":
            # Volver al menú principal
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main_menu()