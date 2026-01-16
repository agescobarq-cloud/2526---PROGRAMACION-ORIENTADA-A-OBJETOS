# modelos/empleado.py
from modelos.persona import Persona


class Empleado(Persona):
    """
    Clase derivada que hereda de Persona.
    Representa a un empleado de una empresa.
    """

    def __init__(self, nombre, edad, cedula, cargo, salario):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, edad, cedula)

        self.cargo = cargo  # atributo público
        self.__salario = salario  # atributo privado (encapsulación)

    # Getter para salario
    def get_salario(self):
        return self.__salario

    # Método sobrescrito → POLIMORFISMO
    def presentarse(self):
        """
        Sobrescritura del método presentarse()
        Muestra comportamiento diferente según el tipo de objeto
        """
        info_padre = super().presentarse()  # llamamos al método original
        return f"{info_padre}. Trabajo como {self.cargo}"

    # Método específico de la clase Empleado
    def aumentar_salario(self, porcentaje):
        if porcentaje > 0:
            aumento = self.__salario * (porcentaje / 100)
            self.__salario += aumento
            print(f"Salario aumentado en {porcentaje}% → Nuevo salario: ${self.__salario:,.2f}")
        else:
            print("El porcentaje de aumento debe ser positivo")

    def __str__(self):
        return f"Empleado: {self.get_nombre()} - Cargo: {self.cargo} - Salario: ${self.__salario:,.2f}"