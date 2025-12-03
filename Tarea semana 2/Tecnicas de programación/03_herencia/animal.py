# animal.py
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("El animal hace un sonido genérico")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")