# main.py
"""
Calculadora de Áreas de Figuras Geométricas
------------------------------------------
Programa interactivo que calcula el área de:
- Cuadrado
- Rectángulo
- Círculo

Utiliza estructura de paquetes con modelos y servicios
"""

from servicios import CalculadoraAreasService


def mostrar_menu():
    print("\n" + "═" * 45)
    print("     CALCULADORA DE ÁREAS DE FIGURAS     ")
    print("═" * 45)
    print("1. Área de Cuadrado")
    print("2. Área de Rectángulo")
    print("3. Área de Círculo")
    print("4. Salir")
    print("═" * 45)


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            CalculadoraAreasService.calcular_y_mostrar_cuadrado()
        elif opcion == "2":
            CalculadoraAreasService.calcular_y_mostrar_rectangulo()
        elif opcion == "3":
            CalculadoraAreasService.calcular_y_mostrar_circulo()
        elif opcion == "4":
            print("\n¡Gracias por usar la calculadora!")
            print("Hasta pronto :)")
            break
        else:
            print("Opción no válida. Por favor ingrese 1, 2, 3 o 4.")


if __name__ == "__main__":
    main()
