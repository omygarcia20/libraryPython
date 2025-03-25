# Lista para almacenar los libros
books = []

def create_book(title, author, isbn):
    # Crea un nuevo libro y lo agrega a la lista de libros.
    # Valida que el ISBN sea único.
    for book in books:
        if book['isbn'] == isbn:
            print("Error: Ya existe un libro con este ISBN.")
            return
    books.append({'title': title, 'author': author, 'isbn': isbn, 'available': True})
    print(f"Libro '{title}' agregado exitosamente.")

def list_books():
    # Muestra la lista de libros disponibles con título, autor, ISBN y disponibilidad.
    if not books:
        print("No hay libros disponibles.")
        return
    print("\n--- Lista de Libros ---")
    for book in books:
        print(f"Título: {book['title']}, Autor: {book['author']}, ISBN: {book['isbn']} Disponible: {book['available']}")

def update_book(isbn, title=None, author=None, available=None):
    # Modifica la información de un libro excepto el ISBN.
    for book in books:
        if book['isbn'] == isbn:
            if title:
                book['title'] = title
            if author:
                book['author'] = author
            if available:
                book['available'] = available
            print(f"Libro con ISBN {isbn} actualizado exitosamente.")
            return
    print("Error: No se encontró un libro con este ISBN.")

def delete_book(isbn):
    # Elimina un libro de la lista.
    for book in books:
        if book['isbn'] == isbn:
            books.remove(book)
            print(f"Libro con ISBN {isbn} eliminado exitosamente.")
            return
    print("Error: No se encontró un libro con este ISBN.")