from users.user import users, create_user, consult_users, update_user, delete_user
from books.book import books, create_book, list_books, update_book, delete_book
from loans.loan import register_loan, list_loans, register_return, delete_loan

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
            book_menu()
        elif case == "3":
            loan_menu()
        elif case == "4":
            print("Saliste del sistema.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# ---------- MENU USUARIOS ----------
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

# ---------- MENU LIBROS ----------
def book_menu():
    # Muestra el menú de gestión de libros.
    while True:
        print("\n--- Gestión de Libros ---")
        print("1. Registrar Libro")
        print("2. Consultar Libros")
        print("3. Modificar Libro")
        print("4. Eliminar Libro")
        print("5. Volver al Menú Principal")
        
        case = input("Seleccione una opción: ")
        
        if case == "1":
            # Registrar libro
            title = input("Ingrese el título: ")
            author = input("Ingrese el autor: ")
            isbn = input("Ingrese el ISBN: ")
            create_book(title, author, isbn)
        elif case == "2":
            # Consultar libros
            list_books()
        elif case == "3":
            # Modificar libro
            isbn = input("Ingrese el ISBN del libro a modificar: ")
            title = input("Nuevo título (dejar en blanco para no modificar): ")
            author = input("Nuevo autor (dejar en blanco para no modificar): ")
            available = input("Disponible (True/False) (dejar en blanco para no modificar): ")
            update_book(isbn, title or None, author or None, available or None)
        elif case == "4":
            # Eliminar libro
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            delete_book(isbn)
        elif case == "5":
            # Volver al menú principal
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# ---------- MENU PRÉSTAMOS ----------
def loan_menu():
    # Muestra el menú de gestión de préstamos.
    while True:
        print("\n--- Gestión de Préstamos ---")
        print("1. Registrar Préstamo")
        print("2. Consultar Préstamos")
        print("3. Registrar Devolución")
        print("4. Eliminar Préstamo")
        print("5. Volver al Menú Principal")
        
        case = input("Seleccione una opción: ")
        
        if case == "1":
            # Registrar préstamo
            user_email = input("Ingrese el correo del usuario: ")
            isbn = input("Ingrese el ISBN del libro: ")
            register_loan(user_email, isbn)
        elif case == "2":
            # Consultar préstamos
            list_loans()
        elif case == "3":
            # Registrar devolución
            loan_id = int(input("Ingrese el código del préstamo a devolver: "))
            register_return(loan_id)
        elif case == "4":
            # Eliminar préstamo
            loan_id = int(input("Ingrese el código del préstamo a eliminar: "))
            delete_loan(loan_id)
        elif case == "5":
            # Volver al menú principal
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main_menu()