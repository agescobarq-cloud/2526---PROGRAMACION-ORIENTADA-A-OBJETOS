# servicios/refugio.py
class Refugio:
    """Clase que gestiona la lógica del refugio (capa de servicios)"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []  # Lista de animales en el refugio

    def agregar_animal(self, animal):
        """Agrega un animal al refugio"""
        self.animales.append(animal)
        print(f"Se ha registrado a {animal.nombre} en {self.nombre}")

    def mostrar_todos_los_animales(self):
        """Muestra información de todos los animales usando polimorfismo"""
        if not self.animales:
            print("El refugio está vacío por ahora... 😢")
            return

        print(f"\nAnimales en {self.nombre}:")
        print("-" * 50)
        for animal in self.animales:
            print(animal.describir())
            print(f"Sonido: {animal.hacer_sonido()}")
            print(f"Estado: {'Adoptado' if animal.adoptado else 'Disponible'}")
            print("-" * 50)

    def adoptar_animal(self, nombre):
        """Busca y marca como adoptado a un animal por su nombre"""
        for animal in self.animales:
            if animal.nombre.lower() == nombre.lower():
                if animal.adoptado:
                    print(f"{nombre} ya fue adoptado anteriormente.")
                else:
                    print(animal.marcar_como_adoptado())
                return
        print(f"No se encontró ningún animal llamado {nombre}")