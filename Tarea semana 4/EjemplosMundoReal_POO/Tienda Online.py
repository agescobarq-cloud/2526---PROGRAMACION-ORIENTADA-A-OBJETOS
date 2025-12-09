# Clase Product: Representa un producto en la tienda.
# Atributos: Nombre, precio y stock disponible.
# Métodos: Para verificar stock y reducirlo al vender.
class Product:
    def __init__(self, name, price, stock):
        self.name = name  # Nombre del producto
        self.price = price  # Precio unitario
        self.stock = stock  # Cantidad disponible

    def is_in_stock(self, quantity):
        # Método para verificar si hay suficiente stock
        return self.stock >= quantity

    def sell(self, quantity):
        # Método para reducir el stock al vender
        if self.is_in_stock(quantity):
            self.stock -= quantity
            return True
        return False


# Clase Cart: Representa el carrito de compras de un cliente.
# Atributos: Lista de items (diccionario con producto y cantidad).
# Métodos: Para agregar/quitar productos y calcular total.
class Cart:
    def __init__(self):
        self.items = {}  # Diccionario: {producto: cantidad}

    def add_product(self, product, quantity):
        # Método para agregar un producto al carrito, verificando stock
        if product.is_in_stock(quantity):
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            product.sell(quantity)  # Interactúa con el producto para reducir stock
            print(f"{quantity} unidades de {product.name} agregadas al carrito.")
        else:
            print(f"No hay suficiente stock de {product.name}.")

    def remove_product(self, product, quantity):
        # Método para quitar un producto del carrito y restaurar stock
        if product in self.items and self.items[product] >= quantity:
            self.items[product] -= quantity
            product.stock += quantity  # Interactúa restaurando stock
            if self.items[product] == 0:
                del self.items[product]
            print(f"{quantity} unidades de {product.name} removidas del carrito.")

    def calculate_total(self):
        # Método para calcular el total del carrito
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total


# Clase Customer: Representa un cliente de la tienda.
# Atributos: Nombre y carrito asociado.
# Métodos: Para finalizar compra y mostrar detalles.
class Customer:
    def __init__(self, name):
        self.name = name  # Nombre del cliente
        self.cart = Cart()  # Cada cliente tiene su propio carrito

    def checkout(self):
        # Método para finalizar la compra: calcula total y vacía el carrito
        total = self.cart.calculate_total()
        if total > 0:
            print(f"Compra finalizada para {self.name}. Total: ${total}")
            self.cart.items.clear()  # Vaciar carrito después de compra
        else:
            print("El carrito está vacío.")


# Ejemplo de uso: Creación de objetos e interacción
product1 = Product("Laptop", 800, 10)  # Crear producto
product2 = Product("Mouse", 20, 50)  # Otro producto

customer = Customer("Ana López")  # Crear cliente con carrito

# Agregar al carrito (interacción: carrito verifica y modifica stock del producto)
customer.cart.add_product(product1, 1)
customer.cart.add_product(product2, 3)

# Calcular total
print(f"Total en carrito: ${customer.cart.calculate_total()}")

# Remover item (interacción: carrito restaura stock)
customer.cart.remove_product(product2, 1)

# Finalizar compra (interacción con carrito)
customer.checkout()

# Verificar stock después de interacciones
print(f"Stock restante de {product1.name}: {product1.stock}")
print(f"Stock restante de {product2.name}: {product2.stock}")