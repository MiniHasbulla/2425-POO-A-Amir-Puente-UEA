# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
import random

# La clase base que utilizare es la clase "Vehículo"
class Vehiculo:
    def __init__(self, tipo, velocidad_maxima):
        self.tipo = tipo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
        else:
            self.velocidad_actual += incremento
        print(f"El {self.tipo} ahora va a {self.velocidad_actual} km/h.")

    def frenar(self, decremento):
        if self.velocidad_actual - decremento < 0:
            self.velocidad_actual = 0
        else:
            self.velocidad_actual -= decremento
        print(f"El {self.tipo} ha reducido la velocidad a {self.velocidad_actual} km/h.")

# Esta es la primera clase derivada, la llame "Piloto"
class Piloto:
    def __init__(self, nombre, equipo, nivel_experiencia):
        self.nombre = nombre
        self.equipo = equipo
        self.nivel_experiencia = nivel_experiencia
        self.puntos = 0
        self.vehiculo = None  # Relación con la clase Vehículo

    def asignar_vehiculo(self, vehiculo):
        self.vehiculo = vehiculo
        print(f"{self.nombre} ha sido asignado al vehículo tipo {vehiculo.tipo}.")

    def competir(self):
        if self.vehiculo:
            rendimiento = random.randint(1, 100) + (self.nivel_experiencia * 2)
            print(f"{self.nombre} está compitiendo... rendimiento: {rendimiento}")
            return rendimiento
        else:
            print(f"{self.nombre} no tiene un vehículo asignado.")
            return 0

    def ganar_puntos(self, puntos_ganados):
        self.puntos += puntos_ganados
        print(f"{self.nombre} ha ganado {puntos_ganados} puntos. Total ahora: {self.puntos} puntos.")

# Esta es otra clase derivada, en este caso me enfoco en la "Carrera"
class Carrera:
    def __init__(self, nombre, distancia):
        self.nombre = nombre
        self.distancia = distancia
        self.participantes = []

    def agregar_participante(self, piloto):
        if piloto.vehiculo:
            self.participantes.append(piloto)
            print(f"{piloto.nombre} ha sido agregado a la carrera {self.nombre}.")
        else:
            print(f"{piloto.nombre} no puede participar sin un vehículo asignado.")

    def iniciar_carrera(self):
        print(f"¡Inicia la carrera {self.nombre}!")
        resultados = []
        for piloto in self.participantes:
            rendimiento = piloto.competir()
            resultados.append((piloto, rendimiento))

        resultados.sort(key=lambda x: x[1], reverse=True)  # Ordenar por rendimiento
        print("\nResultados finales:")
        for idx, (piloto, rendimiento) in enumerate(resultados, start=1):
            puntos_ganados = len(resultados) - idx + 1
            piloto.ganar_puntos(puntos_ganados)
            print(f"{idx}. {piloto.nombre} ({piloto.equipo}) - Rendimiento: {rendimiento}")

# Finalmente coloque pruebas/ejemplos del trabajo
if __name__ == "__main__":
    # Crear vehículos
    vehiculo1 = Vehiculo("Coche Deportivo", 300)
    vehiculo2 = Vehiculo("Moto", 250)

    # Crear pilotos
    piloto1 = Piloto("Daniel", "Toyota GR86", nivel_experiencia=5)
    piloto2 = Piloto("Sam", "BMW M 1000 R 2023", nivel_experiencia=8)

    # Asignar vehículos a los pilotos
    piloto1.asignar_vehiculo(vehiculo1)
    piloto2.asignar_vehiculo(vehiculo2)

    # Crear una carrera
    carrera1 = Carrera("Gran Premio Latinoamericano", distancia=500)

    # Agregar participantes a la carrera
    carrera1.agregar_participante(piloto1)
    carrera1.agregar_participante(piloto2)

    # Iniciar la carrera
    carrera1.iniciar_carrera()
