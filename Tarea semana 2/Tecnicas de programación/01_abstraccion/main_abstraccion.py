# main_abstraccion.py
from circulo import Circulo

circulo = Circulo("Rojo", 5)
print(f"Área: {circulo.calcular_area():.2f}")
print(f"Perímetro: {circulo.calcular_perimetro():.2f}")
circulo.mostrar_color()