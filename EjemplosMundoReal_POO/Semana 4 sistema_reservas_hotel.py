# Sistema de Reservas de Hotel usando Programación Orientada a Objetos

# Clase para representar un cliente
class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}"


# Clase para representar una habitación
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio} - {estado}"


# Clase para representar el hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = {}

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        print("\nHabitaciones disponibles:")
        for hab in self.habitaciones:
            if hab.disponible:
                print(hab)

    def reservar_habitacion(self, cliente, numero_habitacion):
        for hab in self.habitaciones:
            if hab.numero == numero_habitacion and hab.disponible:
                hab.disponible = False
                self.reservas[numero_habitacion] = cliente
                print(f"\nReserva exitosa para {cliente.nombre} en habitación {numero_habitacion}")
                return
        print("\nNo se pudo completar la reserva. Habitación no disponible.")

    def mostrar_reservas(self):
        print("\nReservas actuales:")
        for num, cliente in self.reservas.items():
            print(f"Habitación {num} reservada por {cliente.nombre}")


# -------------------- Simulación --------------------

# Crear hotel
mi_hotel = Hotel("Hotel Paraíso")

# Agregar habitaciones
mi_hotel.agregar_habitacion(Habitacion(101, "Individual", 40))
mi_hotel.agregar_habitacion(Habitacion(102, "Doble", 60))
mi_hotel.agregar_habitacion(Habitacion(103, "Suite", 100))

# Crear cliente
cliente1 = Cliente("Marcos Delgado", "marcos@email.com")

# Mostrar habitaciones disponibles
mi_hotel.mostrar_habitaciones_disponibles()

# Realizar una reserva
mi_hotel.reservar_habitacion(cliente1, 102)

# Mostrar habitaciones después de la reserva
mi_hotel.mostrar_habitaciones_disponibles()

# Mostrar reservas realizadas
mi_hotel.mostrar_reservas()

