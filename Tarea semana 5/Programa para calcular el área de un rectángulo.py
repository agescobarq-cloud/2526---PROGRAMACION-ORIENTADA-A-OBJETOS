# Programa para calcular el área de un rectángulo.
# Este programa solicita al usuario el ancho y alto de un rectángulo, calcula su área y verifica si es un cuadrado.
# Utiliza diferentes tipos de datos: float para dimensiones y área, string para mensajes, boolean para verificación de cuadrado, e integer para un contador simple.

def calcular_area(ancho, alto):
    # Calcula el área multiplicando ancho por alto.
    area = ancho * alto
    # Verifica si es un cuadrado comparando ancho y alto.
    es_cuadrado = ancho == alto
    return area, es_cuadrado

# Solicita input del usuario.
ancho_usuario = float(input("Ingrese el ancho del rectángulo (en unidades): "))
alto_usuario = float(input("Ingrese el alto del rectángulo (en unidades): "))

# Llama a la función para obtener área y verificación.
area_calculada, es_cuadrado = calcular_area(ancho_usuario, alto_usuario)

# Prepara un mensaje string basado en el booleano.
mensaje_forma = "Es un cuadrado." if es_cuadrado else "No es un cuadrado."

# Usa un integer para un contador simple (por ejemplo, número de cálculos realizados).
contador_calculos = 1  # En esta versión simple, solo un cálculo.

# Imprime los resultados.
print(f"El área del rectángulo es: {area_calculada}")
print(mensaje_forma)
print(f"Número de cálculos realizados: {contador_calculos}")