class Libro:
    """Representa un libro en la biblioteca."""

    def __init__(self, titulo: str, autor: str, isbn: str, anio: int = 2023):
        """
        Constructor: Inicializa un nuevo libro con sus datos principales.

        - Obligatorios: título, autor, isbn
        - Opcional: año de publicación (valor por defecto)
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.disponible = True

        print(f"[CREACIÓN] Libro creado → {self.titulo} ({self.isbn})")

    def __del__(self):
        """
        Destructor: se ejecuta cuando el objeto ya no tiene referencias
        (va a ser eliminado por el recolector de basura).

        Aquí simulamos:
        - Registrar que el libro "desapareció" del sistema
        - Podría usarse para: devolver automáticamente, marcar baja, cerrar recursos, etc.
        """
        print(f"[DESTRUCCIÓN] El libro '{self.titulo}' ({self.isbn}) ha sido eliminado del sistema")
        # En un caso real podrías: loggear, actualizar base de datos, etc.

    def __str__(self):
        estado = "disponible" if self.disponible else "prestado"
        return f"{self.titulo} - {self.autor} ({self.anio}) | ISBN: {self.isbn} | {estado}"