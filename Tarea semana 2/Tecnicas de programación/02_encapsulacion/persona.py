# persona.py
class Persona:
    def __init__(self, nombre, edad, email):
        self._nombre = nombre      # protegido
        self._edad = edad
        self._email = None
        self.email = email         # usamos el setter

    # Getter y Setter para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor and valor.strip():
            self._nombre = valor.strip()
        else:
            print("Nombre no válido")

    # Getter y Setter para edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if 0 <= valor <= 120:
            self._edad = valor
        else:
            print("Edad fuera de rango")

    # Getter y Setter para email con validación
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" in valor and "." in valor:
            self._email = valor
        else:
            print("Email inválido")

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, Email: {self._email}")