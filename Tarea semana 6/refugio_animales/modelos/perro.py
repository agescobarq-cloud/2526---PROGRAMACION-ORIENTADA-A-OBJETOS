# modelos/perro.py
from modelos.animal import Animal


class Perro(Animal):
    """Clase derivada que hereda de Animal - representa específicamente perros"""

    def __init__(self, nombre, edad, peso, color, raza, nivel_energia="medio"):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, edad, peso, color)
        self._raza = raza
        self._nivel_energia = nivel_energia

    # Polimorfismo: sobrescritura del método describir
    def describir(self):
        descripcion_base = super().describir()
        return (f"{descripcion_base}. Soy un {self._raza} con nivel de energía "
                f"{self._nivel_energia}")

    # Polimorfismo: implementación específica del método hacer_sonido
    def hacer_sonido(self):
        return "¡Guau guau! 🐶"

    # Método propio de la clase Perro
    def jugar(self, minutos):
        return f"{self._nombre} está jugando felizmente durante {minutos} minutos! ⚡"