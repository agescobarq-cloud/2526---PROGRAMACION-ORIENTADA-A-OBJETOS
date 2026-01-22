from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo


class BibliotecaService:
    """Lógica principal de negocio de la biblioteca"""

    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.prestamos = []

    def registrar_libro(self, titulo, autor, isbn, anio=2023):
        libro = Libro(titulo, autor, isbn, anio)
        self.libros[isbn] = libro
        return libro

    def registrar_usuario(self, nombre, id_usuario, email=None):
        usuario = Usuario(nombre, id_usuario, email)
        self.usuarios[id_usuario] = usuario
        return usuario

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print("Libro no encontrado")
            return None
        if id_usuario not in self.usuarios:
            print("Usuario no encontrado")
            return None

        libro = self.libros[isbn]
        if not libro.disponible:
            print("El libro ya está prestado")
            return None

        usuario = self.usuarios[id_usuario]
        prestamo = Prestamo(libro, usuario)
        self.prestamos.append(prestamo)
        return prestamo

    def devolver_libro(self, prestamo):
        if prestamo in self.prestamos:
            prestamo.cerrar_prestamo()
            self.prestamos.remove(prestamo)