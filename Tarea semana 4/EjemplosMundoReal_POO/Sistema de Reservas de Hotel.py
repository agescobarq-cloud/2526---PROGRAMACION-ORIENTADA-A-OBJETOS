# Clase Room: Representa una habitación en el hotel.
# Atributos: número de habitación, tipo (e.g., 'simple', 'doble'), precio por noche y estado de disponibilidad.
# Métodos: Para verificar disponibilidad y marcar como reservada o libre.
class Room:
    def __init__(self, number, room_type, price):
        self.number = number  # Número único de la habitación
        self.room_type = room_type  # Tipo de habitación (e.g., 'simple', 'doble', 'suite')
        self.price = price  # Precio por noche
        self.available = True  # Estado inicial: disponible

    def is_available(self):
        # Método para verificar si la habitación está disponible
        return self.available

    def reserve(self):
        # Método para marcar la habitación como reservada
        if self.available:
            self.available = False
            return True
        return False

    def release(self):
        # Método para liberar la habitación (marcar como disponible nuevamente)
        self.available = True


# Clase Reservation: Representa una reserva hecha por un cliente.
# Atributos: ID de reserva, cliente, habitación asociada, fechas de check-in y check-out.
# Métodos: Para calcular el costo total y cancelar la reserva (interactuando con la habitación).
class Reservation:
    def __init__(self, reservation_id, customer_name, room, check_in, check_out):
        self.reservation_id = reservation_id  # ID único de la reserva
        self.customer_name = customer_name  # Nombre del cliente
        self.room = room  # Objeto Room asociado
        self.check_in = check_in  # Fecha de entrada (string para simplicidad)
        self.check_out = check_out  # Fecha de salida (string para simplicidad)

    def calculate_cost(self, nights):
        # Método para calcular el costo total basado en el precio de la habitación y noches
        return self.room.price * nights

    def cancel(self):
        # Método para cancelar la reserva, liberando la habitación
        self.room.release()
        print(f"Reserva {self.reservation_id} cancelada. Habitación {self.room.number} liberada.")


# Clase Hotel: Representa el hotel completo, gestionando habitaciones y reservas.
# Atributos: Nombre del hotel, lista de habitaciones y lista de reservas.
# Métodos: Para agregar habitaciones, buscar habitaciones disponibles, crear reservas y mostrar estado.
class Hotel:
    def __init__(self, name):
        self.name = name  # Nombre del hotel
        self.rooms = []  # Lista de objetos Room
        self.reservations = []  # Lista de objetos Reservation

    def add_room(self, room):
        # Método para agregar una habitación al hotel
        self.rooms.append(room)

    def find_available_room(self, room_type):
        # Método para buscar una habitación disponible por tipo
        for room in self.rooms:
            if room.room_type == room_type and room.is_available():
                return room
        return None

    def make_reservation(self, reservation_id, customer_name, room_type, check_in, check_out):
        # Método para crear una reserva: busca habitación disponible, la reserva y la agrega a la lista
        room = self.find_available_room(room_type)
        if room:
            if room.reserve():
                reservation = Reservation(reservation_id, customer_name, room, check_in, check_out)
                self.reservations.append(reservation)
                print(f"Reserva {reservation_id} creada para {customer_name} en habitación {room.number}.")
                return reservation
        print("No hay habitaciones disponibles del tipo solicitado.")
        return None

    def show_status(self):
        # Método para mostrar el estado actual del hotel (habitaciones disponibles)
        available = [room.number for room in self.rooms if room.is_available()]
        print(f"Hotel {self.name} - Habitaciones disponibles: {available}")


# Ejemplo de uso: Creación de objetos e interacción entre ellos
hotel = Hotel("Grand Hotel")  # Crear objeto Hotel
room1 = Room(101, "simple", 100)  # Crear habitación simple
room2 = Room(102, "doble", 150)  # Crear habitación doble
hotel.add_room(room1)  # Agregar habitaciones al hotel
hotel.add_room(room2)

# Hacer una reserva (interacción: hotel busca habitación, crea reserva, modifica estado de habitación)
reservation = hotel.make_reservation(1, "Juan Pérez", "doble", "2025-12-20", "2025-12-25")

# Mostrar estado después de reserva
hotel.show_status()

# Calcular costo (interacción con reserva y habitación)
if reservation:
    cost = reservation.calculate_cost(5)  # 5 noches
    print(f"Costo total: ${cost}")

# Cancelar reserva (interacción: reserva libera la habitación)
if reservation:
    reservation.cancel()

# Mostrar estado después de cancelación
hotel.show_status()