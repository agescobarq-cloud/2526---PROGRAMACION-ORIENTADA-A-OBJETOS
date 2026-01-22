class Usuario:
    """Representa a una persona que puede pedir libros prestados."""

    def __init__(self, nombre: str, id_usuario: str, email: str = None):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.email = email or f"{nombre.lower().replace(' ', '.')}@estudiante.edu"
        self.libros_prestados = 0

        print(f"[CREACIÓN] Usuario registrado → {self.nombre} (ID: {self.id_usuario})")

    def __del__(self):
        print(f"[DESTRUCCIÓN] Usuario {self.nombre} (ID: {self.id_usuario}) ha salido del sistema")

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario}) - Prestados: {self.libros_prestados}"