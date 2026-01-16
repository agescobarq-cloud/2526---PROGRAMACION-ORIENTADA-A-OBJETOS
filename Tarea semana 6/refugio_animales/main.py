# main.py
from modelos.perro import Perro
from servicios.refugio import Refugio


def main():
    print("=== SISTEMA DE GESTIÓN DE REFUGIO DE ANIMALES ===\n")

    # Creamos el refugio
    refugio = Refugio("Refugio Esperanza")

    # Creamos instancias demostrando diferentes casos
    perros = [
        Perro("Rocky", 3, 28, "negro", "Labrador", "alto"),
        Perro("Luna", 1, 8, "blanco", "Schnauzer", "bajo"),
        Perro("Max", 5, 35, "marrón", "Pastor Alemán", "medio")
    ]

    # Agregamos los animales al refugio
    for perro in perros:
        refugio.agregar_animal(perro)

    print("\n" + "=" * 60)
    print("ESTADO INICIAL DEL REFUGIO:")
    refugio.mostrar_todos_los_animales()

    print("\n" + "=" * 60)
    print("PROCESO DE ADOPCIONES:")
    refugio.adoptar_animal("Luna")
    refugio.adoptar_animal("Rocky")
    refugio.adoptar_animal("Firulais")  # Animal que no existe

    print("\n" + "=" * 60)
    print("ESTADO FINAL DEL REFUGIO:")
    refugio.mostrar_todos_los_animales()

    # Demostración adicional de comportamiento específico
    print("\nDemostración de comportamiento específico de Perro:")
    print(perros[0].jugar(30))


if __name__ == "__main__":
    main()