from datetime import datetime
import os


class Prestamo:
    """
    Representa un préstamo activo de un libro a un usuario.
    Demuestra manejo de recursos (archivo abierto).
    """

    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.activo = True

        # Simulamos abrir un log por cada préstamo (para demostrar destructor)
        self.log_path = f"logs/prestamo_{id(self)}.log"
        self.log_file = open(self.log_path, "a", encoding="utf-8")
        self.log_file.write(f"Préstamo iniciado: {datetime.now()}\n")
        self.log_file.write(f"Libro: {libro.titulo} → Usuario: {usuario.nombre}\n\n")

        # Actualizamos contadores
        libro.disponible = False
        usuario.libros_prestados += 1

        print(f"[CREACIÓN] Préstamo creado → {libro.titulo} a {usuario.nombre}")

    def cerrar_prestamo(self):
        """Marca el préstamo como finalizado (devolución)"""
        if not self.activo:
            return
        self.activo = False
        self.libro.disponible = True
        self.usuario.libros_prestados -= 1
        self.log_file.write(f"Préstamo finalizado: {datetime.now()}\n")
        print(f"[DEVOLUCIÓN] {self.libro.titulo} devuelto por {self.usuario.nombre}")

    def __del__(self):
        """
        Destructor: limpia recursos asociados al préstamo.
        - Cierra el archivo de log
        - Registra que el préstamo terminó (aunque no se haya llamado cerrar_prestamo)
        """
        if hasattr(self, 'log_file') and not self.log_file.closed:
            self.log_file.write(f"[DESTRUCCIÓN AUTOMÁTICA] Préstamo terminado abruptamente: {datetime.now()}\n")
            self.log_file.close()
            print(f"[DESTRUCCIÓN] Préstamo cerrado automáticamente (archivo log cerrado)")

        if self.activo:
            print(f"  ⚠️  Préstamo pendiente fue destruido sin devolución formal")