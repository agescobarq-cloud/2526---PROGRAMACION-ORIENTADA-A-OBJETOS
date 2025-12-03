# figura.py
from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def mostrar_color(self):
        print(f"El color es: {self.color}")