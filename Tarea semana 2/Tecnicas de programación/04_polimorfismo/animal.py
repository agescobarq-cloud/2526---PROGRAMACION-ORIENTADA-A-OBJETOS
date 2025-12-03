# animal.py (mismo que antes)
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Sonido genérico")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")