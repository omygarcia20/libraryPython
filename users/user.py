# Lista de usuarios
users = []

# Crear Usuario
def create_user(name, lastName, phone, email, identity):
    
    # Crea un nuevo usuario y lo agrega a la lista users.
    # Verifica que el correo no este duplicado.

    # Validar que todos los campos estén presentes
    if not all([name, lastName, phone, email, identity]):
        print("Todos los campos son obligatorios.")
        return
    # Verificar si el correo ya existe
    for user in users:
        if user["email"] == email:
            print("El usuario ya existe con este correo.")
            return

    # Crear un nuevo usuario como diccionario
    new_user = {
        "name": name,
        "lastName": lastName,
        "phone": phone,
        "email": email,
        "identity": identity
    }
    users.append(new_user)  # Agregar el usuario a la lista
    print(f"El usuario {user['name']} {user['lastName']} fue creado con éxito.")

# Consultar Usuarios
def consult_users():

    # Muestra todos los usuarios registrados en la lista users.
    # Si no hay usuarios, muestra un mensaje indicando que la lista está vacía.

    if not users:
        print("No hay usuarios registrados.")
    else:
        print("Lista de usuarios registrados:")
        for user in users:
            # Mostrar los datos de cada usuario
            print(f"Nombre: {user['name']} {user['lastName']}, Teléfono: {user['phone']}, Correo: {user['email']}, ID: {user['identity']}")

# Modificar Usuario
def update_user(email, name=None, lastName=None, phone=None, new_email=None, identity=None):
    
    # Modifica los datos de un usuario identificado por su correo electrónico.
    # Solo actualiza los campos que se proporcionen como argumentos.

    for user in users:
        if user["email"] == email:  # Buscar el usuario por correo
            # Actualizar los campos proporcionados
            if name:
                user["name"] = name
            if lastName:
                user["lastName"] = lastName
            if phone:
                user["phone"] = phone
            if new_email:
                user["email"] = new_email
            if identity:
                user["identity"] = identity
            print("Usuario modificado con éxito.")
            return
    print("Usuario no encontrado.")  # Si no se encuentra el usuario

# Eliminar Usuario
def delete_user(email):
    # Elimina un usuario identificado por su correo.
    for user in users:
        if user["email"] == email:  # Buscar el usuario por correo
                users.remove(user)  # Eliminar el usuario de la lista
                print("Usuario eliminado con éxito.")
                return
    print("Usuario no encontrado.")  # Si no se encuentra el usuario