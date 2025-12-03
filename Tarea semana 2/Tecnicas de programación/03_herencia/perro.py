# perro.py
from animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):        # Sobrescritura
        print("¡Guau guau!")

    def mostrar_raza(self):
        print(f"Raza: {self.raza}")