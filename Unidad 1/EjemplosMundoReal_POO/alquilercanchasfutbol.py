# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha: 11/01/2025

#Canchas deportivas con especificaciones y disponibilidad
class EspacioDeportivo:
    def __init__(self, nombre, tipo):
        self.nombre =nombre
        self.tipo =tipo
        self.disponibilidad =True
#Guardar la cancha para usarla
    def reservar(self):
        if self.disponibilidad:
            self.disponibilidad =False
            return f"La cancha'{self.nombre}' ha sido reservada"
        else:
            return f"La cancha '{self.nombre}' no se encuentra disponible"
#Eliminar reserva
    def cancelar_reserva(self):
        self.disponibilidad =True
        return f"La reserva de la cancha'{self.nombre}' ha sido cancelada"

#Aqui van los clientes finales que haran uso del programa para reservar la cancha
class Cliente:
    def __init__(self, nombre, email):
        self.nombre =nombre
        self.email =email
        self.reservas =[]
#Reservando
    def hacer_reserva(self, espacio):
        if espacio.disponibilidad:
            espacio.reservar()
            self.reservas.append(espacio)
            return f"El cliente {self.nombre} ha reservado el espacio '{espacio.nombre}'."
        else:
            return f"El espacio '{espacio.nombre}' no está disponible."
#Cancelando
    def cancelar_reserva(self, espacio):
        espacio.cancelar_reserva()
        self.reservas.remove(espacio)
        return f"El cliente {self.nombre} ha cancelado la reserva del espacio '{espacio.nombre}'."

#Sistema general, con espacios y disponibilidad
class SistemaDeReservas:
    def __init__(self):
        self.espacios_disponibles = []
        self.clientes = []

    def agregar_espacio(self, espacio):
        self.espacios_disponibles.append(espacio)

    def ver_disponibilidad(self):
        print("\nDisponibilidad de Espacios Deportivos:")
        for espacio in self.espacios_disponibles:
            disponibilidad = 'Disponible' if espacio.disponibilidad else 'No disponible'
            print(f"{espacio.nombre} ({espacio.tipo}) - {disponibilidad}")

#Probando uno, dos, uno, dos me escuchan
if __name__ == "__main__":
    # Crear espacios deportivos
    espacio1 =EspacioDeportivo("Cancha de Tenis", "Tenis")
    espacio2 =EspacioDeportivo("Cancha de Fútbol", "Fútbol")

#Aqui va el primer cliente del programa
    cliente1 = Cliente("Said Gómez", "saiid_go971@hotmail.com")

#Sistema de reservas y agregar espacios
    sistema_reservas = SistemaDeReservas()
    sistema_reservas.agregar_espacio(espacio1)
    sistema_reservas.agregar_espacio(espacio2)

#Ver disponibilidad
    sistema_reservas.ver_disponibilidad()

#Realizar reservas
    print(cliente1.hacer_reserva(espacio1))
    print(cliente1.hacer_reserva(espacio2))

#Ver disponibilidad después de reservas
    sistema_reservas.ver_disponibilidad()

#Cancelar reservas
    print(cliente1.cancelar_reserva(espacio1))
    print(cliente1.cancelar_reserva(espacio2))

#Ver disponibilidad después de cancelaciones
    sistema_reservas.ver_disponibilidad()