# Funciones para la interfaz en consola
from clases.libro import Libro
from clases.usuario import Usuario
from clases.prestamo import Prestamo


def registrar_libro():
    titulo = input("Título del libro: ")
    autor = input("Autor del libro: ")
    isbn = input("ISBN del libro: ")
    libro = Libro(titulo, autor, isbn)
    return libro


def registrar_usuario():
    nombre = input("Nombre del usuario: ")
    direccion = input("Dirección del usuario: ")
    telefono = input("Teléfono del usuario: ")
    usuario = Usuario(nombre, direccion, telefono)
    return usuario


def registrar_prestamo(usuarios, libros):
    nombre_usuario = input("Nombre del usuario: ")
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print("Usuario no encontrado.")
        return

    titulo_libro = input("Título del libro: ")
    libro = next((l for l in libros if l.titulo == titulo_libro and l.disponible), None)
    if not libro:
        print("Libro no encontrado o no disponible.")
        return

    prestamo = Prestamo(usuario, libro)
    usuario.registrar_prestamo(prestamo)
    libro.disponible = False
    print("Préstamo registrado con éxito.")


def registrar_devolucion(usuarios, libros):
    nombre_usuario = input("Nombre del usuario: ")
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print("Usuario no encontrado.")
        return

    titulo_libro = input("Título del libro: ")
    prestamo = next(
        (
            p
            for p in usuario.prestamos
            if p.libro.titulo == titulo_libro and not p.fecha_devolucion
        ),
        None,
    )
    if not prestamo:
        print("Préstamo no encontrado.")
        return

    prestamo.registrar_devolucion()
    print("Devolución registrada con éxito.")


def mostrar_menu():
    print("\n--- Menú de Gestión de Biblioteca ---")
    print("1. Registrar Libro")
    print("2. Registrar Usuario")
    print("3. Registrar Préstamo")
    print("4. Registrar Devolución")
    print("5. Mostrar Información de Libros")
    print("6. Mostrar Información de Usuarios")
    print("7. Salir")


def main():
    libros = []
    usuarios = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            libro = registrar_libro()
            if libro:
                libros.append(libro)
                print("Libro registrado con éxito.")
        elif opcion == "2":
            usuario = registrar_usuario()
            if usuario:
                usuarios.append(usuario)
                print("Usuario registrado con éxito.")
        elif opcion == "3":
            registrar_prestamo(usuarios, libros)
        elif opcion == "4":
            registrar_devolucion(usuarios, libros)
        elif opcion == "5":
            for libro in libros:
                print(libro.mostrar_informacion())
        elif opcion == "6":
            for usuario in usuarios:
                print(usuario.mostrar_informacion())
                for prestamo in usuario.prestamos:
                    print(prestamo.mostrar_informacion())
        elif opcion == "7":
            print(
                "Saliendo del sistema. ¡Gracias por usar la gestión de la biblioteca!"
            )
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
