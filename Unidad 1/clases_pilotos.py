# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
class Piloto:
    def __init__(self, nombre, equipo, velocidad):
        self.nombre = nombre
        self.equipo = equipo
        self.velocidad = velocidad

    def acelerar(self):
        print(f"{self.nombre} está acelerando con velocidad de {self.velocidad} km/h.")

    def frenar(self):
        print(f"{self.nombre} está frenando.")

#Ejemplificacion
if __name__ == "__main__":
    piloto1 = Piloto("Fernando", "Red Falcon", 180)
    piloto2 = Piloto("Lucía", "Blue Thunder", 200)

    piloto1.acelerar()
    piloto2.frenar()
