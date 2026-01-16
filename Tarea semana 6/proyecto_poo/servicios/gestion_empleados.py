# servicios/gestion_empleados.py
from modelos.empleado import Empleado


class GestionEmpleados:
    """
    Clase de servicio que maneja la lógica de negocio
    relacionada con los empleados
    """

    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        """Agrega un empleado a la lista de gestión"""
        if isinstance(empleado, Empleado):
            self.empleados.append(empleado)
            print(f"Empleado {empleado.get_nombre()} agregado exitosamente")
        else:
            print("Solo se pueden agregar objetos de tipo Empleado")

    def mostrar_todos(self):
        """Muestra información de todos los empleados registrados"""
        if not self.empleados:
            print("No hay empleados registrados aún.")
            return

        print("\n" + "=" * 50)
        print("LISTADO DE EMPLEADOS".center(50))
        print("=" * 50)

        for emp in self.empleados:
            print(emp)
            print("-" * 50)

    def aplicar_aumento_general(self, porcentaje):
        """Demostración de polimorfismo: llama al mismo método en todos los empleados"""
        print(f"\nAplicando aumento general del {porcentaje}% a todos los empleados...")
        for empleado in self.empleados:
            empleado.aumentar_salario(porcentaje)