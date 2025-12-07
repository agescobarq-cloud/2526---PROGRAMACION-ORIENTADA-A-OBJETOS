class Lampara:
    def encender(self):
        print("La lámpara se enciende y da luz brillante 💡")

    def apagar(self):
        print("La lámpara se apaga, todo queda oscuro")


class Ventilador:
    def encender(self):
        print("El ventilador empieza a girar y da aire fresco 🌀")

    def apagar(self):
        print("El ventilador se detiene")


class Televisor:
    def encender(self):
        print("La TV se enciende y muestra imagen y sonido 📺")

    def apagar(self):
        print("La TV se apaga, pantalla en negro")


# USO (el usuario solo sabe que existe "encender" y "apagar")
lampara = Lampara()
ventilador = Ventilador()
tv = Televisor()

lampara.encender()
ventilador.encender()
tv.apagar()