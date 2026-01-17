# servicios/calculadora_areas.py
from modelos import Cuadrado, Rectangulo, Circulo


def obtener_numero_positivo(mensaje: str) -> float:
    """Solicita al usuario un número positivo con validación"""
    while True:
        try:
            numero = float(input(mensaje))
            if numero <= 0:
                print("¡Error! El valor debe ser mayor que cero.")
                continue
            return numero
        except ValueError:
            print("¡Error! Ingrese un número válido.")


class CalculadoraAreasService:
    """Servicio que maneja la lógica de interacción con el usuario y cálculos"""

    @staticmethod
    def calcular_y_mostrar_cuadrado():
        print("\n--- CÁLCULO DE ÁREA DE CUADRADO ---")
        lado = obtener_numero_positivo("Ingrese el lado (m): ")
        figura = Cuadrado(lado)
        print(figura)

    @staticmethod
    def calcular_y_mostrar_rectangulo():
        print("\n--- CÁLCULO DE ÁREA DE RECTÁNGULO ---")
        base = obtener_numero_positivo("Ingrese la base (m): ")
        altura = obtener_numero_positivo("Ingrese la altura (m): ")
        figura = Rectangulo(base, altura)
        print(figura)

    @staticmethod
    def calcular_y_mostrar_circulo():
        print("\n--- CÁLCULO DE ÁREA DE CÍRCULO ---")
        radio = obtener_numero_positivo("Ingrese el radio (m): ")
        figura = Circulo(radio)
        print(figura)