import os
import subprocess
from datetime import datetime

NOMBRE_COMPLETO = "Angel Gabriel Escobar Quesada"
CARRERA = "Ingeniería en Tecnologías de la Información"
CURSO = "Programación Orientada a Objetos - 2025-2026"
MENSAJE_BIENVENIDA = f"Bienvenido al Dashboard POO de Angel Gabriel Escobar Quesada"

def mostrar_codigo(ruta_script):
    ruta_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n{'═' * 70}")
            print(f"--- Código fuente: {os.path.basename(ruta_script)} ---")
            print(f"{'═' * 70}\n")
            print(codigo)
            print(f"{'═' * 70}\n")
            return codigo
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_script}'")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        print(f"Ejecutando: {os.path.basename(ruta_script)} ...\n")
        if os.name == 'nt':
            subprocess.Popen(['cmd', '/k', 'python', ruta_script], shell=True)
        else:
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
        print("→ Script lanzado en una nueva ventana.")
    except Exception as e:
        print(f"No se pudo ejecutar el script: {e}")
        print("→ Verifica que Python esté en el PATH y que el archivo sea válido.")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1 - Introducción a POO',
        '2': 'Unidad 2 - Clases y Objetos',
    }

    while True:
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"\n{'═' * 60}")
        print(f"  {MENSAJE_BIENVENIDA}")
        print(f"  {CURSO}  |  {fecha_actual}")
        print(f"{'═' * 60}\n")

        for key, valor in unidades.items():
            print(f"  {key} → {valor}")
        print("  0 → Salir del Dashboard\n")

        eleccion = input("   Elige una unidad (o 0 para salir): ").strip()

        if eleccion == '0':
            print("\n¡Gracias por usar el Dashboard POO!")
            print(f"Hasta pronto, {NOMBRE_COMPLETO} 👋\n")
            break
        elif eleccion in unidades:
            ruta_unidad = os.path.join(ruta_base, f"Unidad {eleccion}")
            if not os.path.exists(ruta_unidad):
                ruta_unidad = os.path.join(ruta_base, unidades[eleccion].split('-')[0].strip())
            mostrar_sub_menu(ruta_unidad, unidades[eleccion])
        else:
            print("Opción no válida. Intenta de nuevo.\n")

def mostrar_sub_menu(ruta_unidad, nombre_unidad):
    if not os.path.exists(ruta_unidad):
        print(f"\nNo se encontró la carpeta: {ruta_unidad}")
        print("→ Verifica que las carpetas estén creadas correctamente.")
        input("\nPresiona Enter para continuar...")
        return

    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print(f"\n{'─' * 60}")
        print(f"  {nombre_unidad}")
        print(f"  Carpeta: {os.path.basename(ruta_unidad)}")
        print(f"{'─' * 60}\n")

        if not sub_carpetas:
            print("  (No hay subcarpetas/temas en esta unidad aún)\n")
        else:
            for i, carpeta in enumerate(sub_carpetas, 1):
                print(f"  {i} → {carpeta}")

        print("\n  0 → Volver al menú principal\n")

        eleccion = input("   Elige un tema (o 0 para regresar): ").strip()

        if eleccion == '0':
            break
        else:
            try:
                idx = int(eleccion) - 1
                if 0 <= idx < len(sub_carpetas):
                    carpeta_elegida = sub_carpetas[idx]
                    ruta_completa = os.path.join(ruta_unidad, carpeta_elegida)
                    mostrar_scripts(ruta_completa, carpeta_elegida)
                else:
                    print("Número fuera de rango. Intenta de nuevo.")
            except ValueError:
                print("Ingresa un número válido.")

def mostrar_scripts(ruta_carpeta, nombre_carpeta):
    scripts = [f.name for f in os.scandir(ruta_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\n{'─' * 60}")
        print(f"  Ejercicios / Scripts → {nombre_carpeta}")
        print(f"{'─' * 60}\n")

        if not scripts:
            print("  (No hay scripts .py en esta carpeta)\n")
        else:
            for i, script in enumerate(scripts, 1):
                print(f"  {i} → {script}")

        print("\n  0 → Volver al menú de temas")
        print("  9 → Volver al menú principal\n")

        eleccion = input("   Elige un script (0 o 9 para regresar): ").strip()

        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        else:
            try:
                idx = int(eleccion) - 1
                if 0 <= idx < len(scripts):
                    script_elegido = scripts[idx]
                    ruta_script = os.path.join(ruta_carpeta, script_elegido)

                    print(f"\n→ Seleccionado: {script_elegido}")
                    codigo = mostrar_codigo(ruta_script)

                    if codigo:
                        resp = input("\n¿Quieres EJECUTAR este script ahora? (s/n): ").strip().lower()
                        if resp in ['s', 'si', 'y', 'yes', '1']:
                            ejecutar_codigo(ruta_script)
                            input("\nPresiona Enter cuando termines de ver el resultado...")
                        else:
                            print("→ No se ejecutó el script.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor ingresa un número.")

if __name__ == "__main__":
    print("Iniciando Dashboard POO personalizado...")
    mostrar_menu()
