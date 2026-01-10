# Pequeño programa que registra información básica de un estudiante,
# calcula su promedio de notas y determina si aprobó o reprobó la materia.
# Demuestra el uso de diferentes tipos de datos y la convención snake_case.

# ==================== ENTRADA DE DATOS ====================

# Datos de tipo string (texto)
nombre_completo = input("Ingrese el nombre completo del estudiante: ")
materia = input("Ingrese el nombre de la materia: ")

# Datos de tipo entero (integer)
edad = int(input("Ingrese la edad del estudiante: "))

# Datos de tipo flotante (float) - notas
nota1 = float(input("Ingrese la primera nota (0-10): "))
nota2 = float(input("Ingrese la segunda nota (0-10): "))
nota3 = float(input("Ingrese la tercera nota (0-10): "))

# Bandera booleana (boolean) - la inicializamos en False
es_mayor_de_edad = False

# ==================== PROCESAMIENTO ====================

# Decisión simple con boolean
if edad >= 18:
    es_mayor_de_edad = True

# Cálculo del promedio (float)
promedio = (nota1 + nota2 + nota3) / 3

# Determinar si aprobó (usamos redondeo a 2 decimales)
promedio_redondeado = round(promedio, 2)
aprobo = promedio_redondeado >= 7.0

# Mensaje final según resultado
if aprobo:
    resultado = "APROBADO"
    emoji_resultado = "🎉"
else:
    resultado = "REPROBADO"
    emoji_resultado = "😔"

# ==================== SALIDA DE RESULTADOS ====================

print("\n" + "="*50)
print("          REGISTRO DEL ESTUDIANTE")
print("="*50)
print(f"Nombre completo:     {nombre_completo}")
print(f"Materia:             {materia}")
print(f"Edad:                {edad} años", end=" ")
if es_mayor_de_edad:
    print("(mayor de edad)")
else:
    print("(menor de edad)")
print(f"Notas ingresadas:    {nota1}  -  {nota2}  -  {nota3}")
print(f"Promedio final:      {promedio_redondeado}")
print(f"Estado de la materia: {resultado} {emoji_resultado}")
print("="*50)

# Mensaje motivacional según resultado :)
if aprobo:
    print("¡Felicidades! Sigue así, vas muy bien ☺️")
else:
    print("No te desanimes, la próxima vez será mejor 💪")
    print(f"Necesitas mejorar {7 - promedio_redondeado:.2f} puntos aproximadamente")