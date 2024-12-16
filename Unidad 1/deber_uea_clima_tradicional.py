# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
#Aqui defino la función para temperaturas
#Para los siete dias de la semana
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Digita la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

#Aqui va el calculo del promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

#Finalmente enseño el programa
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()