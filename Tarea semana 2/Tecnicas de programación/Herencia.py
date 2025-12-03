class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")


# HERENCIA: Estudiante hereda todo de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # reutilizamos el constructor de Persona
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}")


# Uso
est = Estudiante("Carlos", 20, "Ingeniería")
est.presentarse()  # → Método heredado
est.estudiar()  # → Método propio de Estudiante