# Programación Tradicional: Gestión del promedio semanal del clima
# Este enfoque usa variables globales y funciones para organizar el código de manera procedural.
# Limitaciones: Dependencia de variables globales, lo que puede complicar el mantenimiento en programas más grandes.

# Variable global para almacenar las temperaturas diarias (una por día durante 7 días)
temperaturas = []

# Función para ingresar las temperaturas diarias
# Solicita al usuario ingresar 7 temperaturas, una por día, y las almacena en la lista global.
def ingresar_temperaturas():
    global temperaturas  # Acceso a la variable global
    for dia in range(1, 8):  # Días de la semana (1 a 7)
        temp = float(input(f"Ingrese la temperatura para el día {dia}: "))  # Entrada del usuario
        temperaturas.append(temp)  # Agregar a la lista

# Función para calcular el promedio semanal
# Calcula el promedio de las temperaturas almacenadas en la lista global.
def calcular_promedio():
    global temperaturas  # Acceso a la variable global
    if len(temperaturas) == 0:  # Manejo de caso vacío
        return 0.0
    suma = sum(temperaturas)  # Suma de todas las temperaturas
    promedio = suma / len(temperaturas)  # Cálculo del promedio
    return promedio

# Uso principal del programa
# Llama a las funciones en secuencia para ejecutar el programa.
ingresar_temperaturas()  # Ingresar datos
promedio_semanal = calcular_promedio()  # Calcular promedio
print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}°C")  # Imprimir resultado con 2 decimales