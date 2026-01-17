# modelos/figuras.py
from math import pi


class Figura:
    """Clase base abstracta para figuras geométricas"""

    def calcular_area(self):
        """Método que deben implementar las clases hijas"""
        raise NotImplementedError("Este método debe ser implementado por la clase hija")


class Cuadrado(Figura):
    """Representa un cuadrado geométrico"""

    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un número positivo")
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def __str__(self) -> str:
        return f"Cuadrado (lado = {self.lado:.2f}) → Área = {self.calcular_area():.2f} m²"


class Rectangulo(Figura):
    """Representa un rectángulo geométrico"""

    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser números positivos")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def __str__(self) -> str:
        return f"Rectángulo ({self.base:.2f} × {self.altura:.2f}) → Área = {self.calcular_area():.2f} m²"


class Circulo(Figura):
    """Representa un círculo geométrico"""

    def __init__(self, radio: float):
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo")
        self.radio = radio

    def calcular_area(self) -> float:
        return pi * self.radio ** 2

    def __str__(self) -> str:
        return f"Círculo (radio = {self.radio:.2f}) → Área = {self.calcular_area():.2f} m²"