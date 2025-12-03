# main_polimorfismo.py
from perro import Perro
from gato import Gato

animales = [
    Perro("Firulais", 3),
    Gato("Michi", 2),
    Perro("Luna", 1)
]

print("=== Demostración de Polimorfismo ===\n")
for animal in animales:
    animal.mostrar_info()
    animal.hacer_sonido()
    print("-" * 30)