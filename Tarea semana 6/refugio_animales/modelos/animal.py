# modelos/animal.py
class Animal:
    """Clase base que representa cualquier animal en el refugio"""

    def __init__(self, nombre, edad, peso, color):
        # Encapsulación: atributos protegidos (convención con _)
        self._nombre = nombre
        self._edad = edad
        self._peso = peso
        self._color = color
        self._adoptado = False

    # Getters (métodos para acceder a atributos protegidos)
    @property
    def nombre(self):
        return self._nombre

    @property
    def adoptado(self):
        return self._adoptado

    def describir(self):
        """Método común que será sobrescrito (polimorfismo)"""
        return (f"Soy {self._nombre}, un animal de {self._edad} años, "
                f"peso {self._peso}kg, color {self._color}")

    def hacer_sonido(self):
        """Método abstracto - cada animal hará su sonido característico"""
        return "Sonido genérico de animal..."

    def marcar_como_adoptado(self):
        """Cambia el estado del animal a adoptado"""
        self._adoptado = True
        return f"¡{self._nombre} ha sido adoptado! 🏡"