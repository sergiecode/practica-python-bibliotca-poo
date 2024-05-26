from datetime import datetime


class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = None

    def registrar_devolucion(self):
        self.fecha_devolucion = datetime.now()
        self.libro.disponible = True

    def mostrar_informacion(self):
        fecha_devolucion = (
            self.fecha_devolucion if self.fecha_devolucion else "No devuelto"
        )
        return f"Usuario: {self.usuario.nombre}, Libro: {self.libro.titulo}, Fecha de Préstamo: {self.fecha_prestamo}, Fecha de Devolución: {fecha_devolucion}"
