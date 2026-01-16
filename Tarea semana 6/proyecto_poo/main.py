# main.py
from modelos.empleado import Empleado
from servicios.gestion_empleados import GestionEmpleados


def main():
    print("=== SISTEMA DE GESTIÓN DE EMPLEADOS ===\n")

    # Crear servicio de gestión
    gestion = GestionEmpleados()

    # Crear instancias de las clases (demostración)
    emp1 = Empleado("María Pérez", 28, "1723456789", "Desarrolladora", 1450.00)
    emp2 = Empleado("Carlos Ramírez", 35, "1809876543", "Analista", 1680.50)
    emp3 = Empleado("Ana Torres", 42, "1712345678", "Gerente de Proyectos", 2450.75)

    # Agregar empleados al sistema
    gestion.agregar_empleado(emp1)
    gestion.agregar_empleado(emp2)
    gestion.agregar_empleado(emp3)

    print("\nPresentación de cada empleado (POLIMORFISMO):")
    print("-" * 60)
    print(emp1.presentarse())
    print(emp2.presentarse())
    print(emp3.presentarse())

    # Mostrar listado inicial
    gestion.mostrar_todos()

    # Demostración de encapsulación y setters
    print("\nIntentando modificar edad directamente (no posible):")
    # emp1.__edad = 500  # Esto NO funciona por encapsulación
    emp1.set_edad(29)  # Esta es la forma correcta

    # Aplicar aumento general (polimorfismo)
    gestion.aplicar_aumento_general(8.5)

    # Mostrar resultado final
    print("\nESTADO FINAL DESPUÉS DEL AUMENTO:")
    gestion.mostrar_todos()


if __name__ == "__main__":
    main()