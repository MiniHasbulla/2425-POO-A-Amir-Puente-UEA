# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
#Declaro las clases requeridas
class ClimaDiario:
    def __init__(self):
        self.temperaturas = []
#La clase registra las temperaturas
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Digita la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)
#Clase para obtener el promedio
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

#El programa de manera general
def main():
    clima = ClimaDiario()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
