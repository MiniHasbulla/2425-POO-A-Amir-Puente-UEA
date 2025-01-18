#"Universidad Estatal Amazonica"
#Clase: POO Paralelo A
#Nombre: Amir Puente
#Fecha: 18/01/2025
#Tema: Trabajo Semana 6 Pilares de POO

#Aqui creo la clase base llamada Vehiculo, esta servira de plantilla para los carros
class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca =marca  #La marca va como público
        self.__modelo =modelo  # El modelo lo coloco como privado
        self.__velocidad_maxima =velocidad_maxima

#Este metodo me permite llamar al modelo del carro
    def get_modelo(self):
        return self.__modelo
#Similar al anterior pero esta vez es para conseguir la velocidad maxima
    def get_velocidad_maxima(self):
        return self.__velocidad_maxima

#Aqui se diferencia de las anteriores ya que se escribe en las clases derivadas
    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.__modelo}, Velocidad Máxima: {self.__velocidad_maxima} km/h"

#Ahora bien, aqui creo una clase aparte exclusivament para el motor
class Motor:
    def __init__(self, tipo_motor, potencia):
        self.tipo_motor =tipo_motor  #Lo designo como público
        self.__potencia =potencia  #Este como privado

#Obtengo la potencia del vehiculo
    def get_potencia(self):
        return self.__potencia
#Este se escribe en las clases hijas
    def mostrar_motor_info(self):
        return f"Tipo de Motor: {self.tipo_motor}, Potencia: {self.__potencia} HP"
#Clase derivada coche que hereda de vehiculo y motor
class Coche(Vehiculo, Motor):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_motor, potencia, num_puertas):
        Vehiculo.__init__(self, marca, modelo, velocidad_maxima)
        Motor.__init__(self, tipo_motor, potencia)
        self.num_puertas = num_puertas

#Sobrescribo mostrar_info para los coches
    def mostrar_info(self):
        return f"{Vehiculo.mostrar_info(self)}, Número de Puertas: {self.num_puertas}"
    def mostrar_motor_info(self):
        return f"{Motor.mostrar_motor_info(self)}, Ideal para coches."

#Clase derivada motocicleta que hereda de vehiculo y motor
class Motocicleta(Vehiculo, Motor):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_motor, potencia, tiene_carroceria):
        Vehiculo.__init__(self, marca, modelo, velocidad_maxima)
        Motor.__init__(self, tipo_motor, potencia)
        self.tiene_carroceria = tiene_carroceria

#Sobrescribo mostrar_info para motocicleta
    def mostrar_info(self):
        return f"{Vehiculo.mostrar_info(self)}, Tiene carrocería: {self.tiene_carroceria}"
    def mostrar_motor_info(self):
        return f"{Motor.mostrar_motor_info(self)}, Ideal para motocicletas."

#Esta función la coloco para demostrar el polimorfismo
def mostrar_datos_vehiculo(vehiculo):
    print(vehiculo.mostrar_info())
    print(vehiculo.mostrar_motor_info())

#En esta seccion van las instancias de los vehículos
coche= Coche("BMW", "M3 E30 Sport Evolution", 248, "Gasolina", 238, 2)
motocicleta= Motocicleta("Yamaha", "YZF-R3", 200, "Gasolina", 50, True)

#Finalmente muestro en pantalla
print("Información general del coche:")
mostrar_datos_vehiculo(coche)

print("\nInformación general de la motocicleta:")
mostrar_datos_vehiculo(motocicleta)
