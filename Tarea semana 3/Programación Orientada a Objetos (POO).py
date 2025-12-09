# Programación Orientada a Objetos (POO): Gestión del promedio semanal del clima
# Este enfoque usa una clase para encapsular datos y comportamientos, promoviendo reutilización y modularidad.
# Beneficios: Encapsulamiento (oculta detalles internos), lo que mejora el mantenimiento y reduce errores.

class ClimaSemanal:
    # Constructor de la clase
    # Inicializa la lista de temperaturas como atributo privado (encapsulamiento).
    def __init__(self):
        self.__temperaturas = []  # Atributo privado: lista de temperaturas diarias (no accesible directamente desde fuera)

    # Método para agregar una temperatura diaria
    # Permite ingresar temperaturas una por una, manteniendo el encapsulamiento.
    def agregar_temperatura(self, temp):
        self.__temperaturas.append(temp)  # Agregar a la lista privada

    # Método para ingresar todas las temperaturas de la semana
    # Solicita al usuario ingresar 7 temperaturas y las agrega usando el método agregar_temperatura.
    def ingresar_temperaturas(self):
        for dia in range(1, 8):  # Días de la semana (1 a 7)
            temp = float(input(f"Ingrese la temperatura para el día {dia}: "))  # Entrada del usuario
            self.agregar_temperatura(temp)  # Usar el método para agregar

    # Método para calcular el promedio semanal
    # Accede al atributo privado para calcular y retornar el promedio.
    def calcular_promedio(self):
        if len(self.__temperaturas) == 0:  # Manejo de caso vacío
            return 0.0
        suma = sum(self.__temperaturas)  # Suma de temperaturas
        promedio = suma / len(self.__temperaturas)  # Cálculo del promedio
        return promedio

# Uso principal del programa
# Crea un objeto de la clase y llama a sus métodos.
clima = ClimaSemanal()  # Instanciar el objeto
clima.ingresar_temperaturas()  # Ingresar datos
promedio_semanal = clima.calcular_promedio()  # Calcular promedio
print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}°C")  # Imprimir resultado con 2 decimales