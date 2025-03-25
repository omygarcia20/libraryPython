# Library system

Este proyecto es un sistema de gestión de biblioteca desarrollado en Python. Permite gestionar libros, usuarios y préstamos.
---
## Funcionalidades principales


### 1. Gestión de Usuarios
- **Registrar Usuario:** Permite agregar un nuevo usuario al sistema. Cada usuario tiene un nombre, apellido, teléfono, correo electrónico único y un número de identificación.
- **Consultar Usuarios:** Muestra una lista de todos los usuarios registrados, incluyendo su nombre, apellido, correo electrónico y número de identificación.
- **Actualizar Usuario:** Permite modificar la información de un usuario (nombre, apellido, teléfono, correo electrónico o identificación) utilizando su correo electrónico.
- **Eliminar Usuario:** Permite eliminar un usuario del sistema utilizando su correo electrónico.

### 2. Gestión de Libros
- **Registrar Libro:** Permite agregar un nuevo libro a la biblioteca. Cada libro tiene un título, autor, ISBN único y un estado de disponibilidad.
- **Consultar Libros:** Muestra una lista de todos los libros registrados, incluyendo su título, autor, ISBN y si están disponibles.
- **Actualizar Libro:** Permite modificar la información de un libro (título, autor o disponibilidad) utilizando su ISBN.
- **Eliminar Libro:** Permite eliminar un libro de la biblioteca utilizando su ISBN.

### 3. Gestión de Préstamos
- **Registrar Préstamo:** Permite registrar un préstamo de un libro a un usuario. Cada préstamo tiene un código único autoincrementado (`loan_id`), el usuario, el libro, la fecha de préstamo y un estado de devolución.
  - Valida que el usuario esté registrado.
  - Valida que el libro esté disponible.
  - Muestra el código del préstamo al registrarlo.
- **Consultar Préstamos:** Muestra una lista de todos los préstamos activos, incluyendo el código del préstamo, el usuario, el libro y la fecha de préstamo.
- **Registrar Devolución:** Permite registrar la devolución de un libro utilizando el código del préstamo (`loan_id`). Actualiza el estado del préstamo y marca el libro como disponible.
- **Eliminar Préstamo:** Permite eliminar un préstamo utilizando su código (`loan_id`). Si el préstamo no tiene devolución registrada, también actualiza la disponibilidad del libro.

---
