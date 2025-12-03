# main_encapsulacion.py
from persona import Persona

p = Persona("Ana", 25, "ana@gmail.com")
p.mostrar_info()

p.edad = 30
p.email = "correo_malo"   # no se acepta
p.email = "nuevo@dominio.com"
p.mostrar_info()