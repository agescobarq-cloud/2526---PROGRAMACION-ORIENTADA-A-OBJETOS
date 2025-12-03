class Gato:
    def hablar(self):
        print("¡Miau!")


class Perro:
    def hablar(self):
        print("¡Guau!")


class Vaca:
    def hablar(self):
        print("¡Muuu!")


# POLIMORFISMO: mismo método, diferente comportamiento
def hacer_hablar(animal):
    animal.hablar()  # No importa de qué clase sea, siempre llama al método correcto


# Uso
animales = [Gato(), Perro(), Vaca()]

for animal in animales:
    hacer_hablar(animal)

# Salida:
# ¡Miau!
# ¡Guau!
# ¡Muuu!