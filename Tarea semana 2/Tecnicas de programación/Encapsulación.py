class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # privado (nadie puede tocarlo directamente)

    # Getter
    def obtener_saldo(self):
        return self.__saldo

    # Setter con validación
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositado {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("Cantidad no válida")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retirado {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida")


# Uso
cuenta = CuentaBancaria("Ana")
cuenta.depositar(1000)
cuenta.retirar(300)
print(cuenta.obtener_saldo())  # → 700
# print(cuenta.__saldo)  # Error! Está encapsulado