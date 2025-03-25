from datetime import datetime
from books.book import books  # Importa la lista de libros desde book.py
from users.user import users  # Importa la lista de usuarios desde user.py

# Lista para almacenar los préstamos
loans = []
next_loan_id = 1  # Variable global para manejar el ID autoincrementado de los préstamos

def register_loan(user_email, isbn):
    # Registra un préstamo de un libro a un usuario.
    # Valida que el usuario esté registrado y que el libro esté disponible.
    global next_loan_id
    # Busca el usuario por correo electrónico
    for user in users:
        if user['email'] == user_email:
            # Busca el libro por ISBN en la lista de libros
            for book in books:
                if book['isbn'] == isbn:
                    if not book['available']:
                        print(f"Error: El libro '{book['title']}' no está disponible para préstamo.")
                        return
                    # Crear el préstamo con un código único
                    loan = {
                        'loan_id': next_loan_id,
                        'user': user,
                        'book': book,
                        'loan_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'return_date': None
                    }
                    loans.append(loan)
                    book['available'] = False  # Marca el libro como no disponible
                    print(f"Préstamo registrado exitosamente. Código del préstamo: {next_loan_id}")
                    print(f"Libro '{book['title']}' prestado a {user['name']} {user['lastName']}.")
                    next_loan_id += 1  # Incrementa el ID para el próximo préstamo
                    return
            print(f"Error: No se encontró un libro con el ISBN {isbn}.")
            return
    print(f"Error: No se encontró un usuario con el correo {user_email}.")


def list_loans():
    # Muestra la lista de préstamos activos con usuario, libro y fecha de préstamo.
    if not loans:
        print("No hay préstamos activos.")
        return
    print("\n--- Lista de Préstamos Activos ---")
    for loan in loans:
        if loan['return_date'] is None:
            print(f"Código del Préstamo: {loan['loan_id']}, Usuario: {loan['user']['name']} {loan['user']['lastName']}, "
                  f"Libro: {loan['book']['title']}, Fecha de Préstamo: {loan['loan_date']}")


def register_return(loan_id):
    # Registra la devolución de un libro y actualiza su disponibilidad.
    # Busca el préstamo activo por loan_id
    for loan in loans:
        if loan['loan_id'] == loan_id and loan['return_date'] is None:
            # Actualiza la fecha de devolución
            loan['return_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            loan['book']['available'] = True  # Marca el libro como disponible
            print(f"Devolución registrada exitosamente. Libro '{loan['book']['title']}' devuelto.")
            return
    print(f"Error: No se encontró un préstamo activo con el código {loan_id}.")


def delete_loan(loan_id):
    # Elimina un préstamo de la lista en caso de error o cancelación.
    # Busca el préstamo por loan_id
    for loan in loans:
        if loan['loan_id'] == loan_id:
            loans.remove(loan)
            if loan['return_date'] is None:
                loan['book']['available'] = True  # Marca el libro como disponible si no se devolvió
            print(f"Préstamo del libro '{loan['book']['title']}' con código {loan_id} eliminado exitosamente.")
            return
    print(f"Error: No se encontró un préstamo con el código {loan_id}.")