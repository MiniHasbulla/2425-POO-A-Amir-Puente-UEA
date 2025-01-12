#"Universidad Estatal Amazonica"
#Clase: POO Paralelo A
#Nombre: Amir Puente
#Fecha:11/01/2025

#Para dar cumplimiento al deber solicitado decidi crear un programa
#que gestione las puntuaciones de un torneo de videojuegos.
#Principalmente se permite registrar jugadores, actualizar sus puntuaciones
#y ver el ranking de jugadores basado en las puntuaciones más altas

class Jugador:
#Clase del jugador, con sus atributos y metodos
    def __init__(self, nombre, puntuacion_inicial):
        self.nombre =nombre
        self.puntuacion =puntuacion_inicial
        self.calificado =False

    def actualizar_puntuacion(self, nueva_puntuacion):
#Sirve para actualizar la puntuacion
        if nueva_puntuacion >=0:
            self.puntuacion =nueva_puntuacion
            print(f"La puntuación del jugador {self.nombre} ha sido actualizada a {self.puntuacion}.")
        else:
            print("La puntuación no puede ser negativa")
#Esto permite clasificar a los jugadores con puntaje minimo para clasificar
    def verificar_calificacion(self, puntaje_minimo):
        if self.puntuacion >=puntaje_minimo:
            self.calificado =True
            print(f"{self.nombre} ha calificado al torneo")
        else:
            self.calificado = False
            print(f"{self.nombre} no califico al torneo")
#Devuelvo la cadena del jugador
    def __str__(self):
        estado_calificado = "Calificado" if self.calificado else "No calificado"
        return f"{self.nombre} - Puntuación: {self.puntuacion} - Estado: {estado_calificado}"

#Aqui muestro el ranking o clasificacion
def mostrar_ranking(jugadores):

#Ordeno de mayor a menor
    jugadores_ordenados = sorted(jugadores, key=lambda x: x.puntuacion, reverse=True)

    print("\nRanking del Torneo:")
    for i, jugador in enumerate(jugadores_ordenados, 1):
        print(f"{i}. {jugador}")

#Principal para probar
def main():
    jugadores =[]

#Registro
    jugador1 = Jugador("Matias", 1630)
    jugador2 = Jugador("Isabelle", 870)
    jugador3 = Jugador("Juan", 1380)
    jugador4 = Jugador("Camila", 2090)

#Lista
    jugadores.append(jugador1)
    jugadores.append(jugador2)
    jugadores.append(jugador3)
    jugadores.append(jugador4)

#Puntaje jugadores
    puntaje_minimo = 1500
    for jugador in jugadores:
        jugador.verificar_calificacion(puntaje_minimo)

#Indicar ranking
    mostrar_ranking(jugadores)

#Prueba de actualizar puntuación
    jugador1.actualizar_puntuacion(1900)

#Volver a verificar
    jugador1.verificar_calificacion(puntaje_minimo)

#Mostrar el ranking
    mostrar_ranking(jugadores)

if __name__ == "__main__":
    main()
