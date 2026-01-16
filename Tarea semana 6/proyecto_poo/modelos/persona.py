# modelos/persona.py
class Persona:
    """
    Clase base que representa a una persona genérica.
    Demuestra ENCAPSULACIÓN mediante atributos privados.
    """

    def __init__(self, nombre, edad, cedula):
        # Atributos privados (encapsulación) usando doble guion bajo
        self.__nombre = nombre  # privado
        self.__edad = edad  # privado
        self.__cedula = cedula  # privado

    # Getters (métodos para obtener valores de atributos privados)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_cedula(self):
        return self.__cedula

    # Setter (método para modificar edad con validación)
    def set_edad(self, nueva_edad):
        if nueva_edad > 0 and nueva_edad < 120:
            self.__edad = nueva_edad
        else:
            print("Edad no válida (debe estar entre 1 y 119 años)")

    # Método común que será sobrescrito (POLIMORFISMO)
    def presentarse(self):
        """Método que será sobrescrito en clases hijas"""
        return f"Soy {self.__nombre}, tengo {self.__edad} años"

    def __str__(self):
        return f"Persona: {self.__nombre} - Cédula: {self.__cedula}"