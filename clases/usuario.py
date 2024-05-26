class Usuario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.prestamos = []

    def actualizar_informacion(self, direccion=None, telefono=None):
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono

    def registrar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def mostrar_informacion(self):
        return f"Usuario: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"
