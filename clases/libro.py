class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def actualizar_informacion(self, titulo=None, autor=None, isbn=None):
        if titulo:
            self.titulo = titulo
        if autor:
            self.autor = autor
        if isbn:
            self.isbn = isbn

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"
