#"Universidad Estatal Amazonica"
#Clase: POO Paralelo A
#Nombre: Amir Puente
#Fecha: 18/01/2025
#Tema: Trabajo Semana 6 Pilares de POO

#Esta es la clase base, es decir la clase Empleado, defino sus caracteristicas
class Empleado:
    def __init__(self, nombre, edad, salario):
        # Atributos protegidos (Encapsulación)
        self._nombre =nombre
        self._edad =edad
        self._salario =salario
#Metodo para conseguir la informacion
    def obtener_informacion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Salario: {self._salario}"
#Metodo para ver su sueldo anual
    def calcular_salario_anual(self):
        return self._salario * 12

#Metodo sobrescrito
    def tipo_empleado(self):
        return "Empleado"

#Aqui coloco la primera clase derivada, esta sera la Gerente
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)  #Hago uso del constructor
        self._departamento =departamento  #Atributos específicos

#Sobrescribir tipo_empleado para designarlo como Gerente
    def tipo_empleado(self):
        return "Gerente"

#Metodo para departamento
    def obtener_departamento(self):
        return self._departamento

#Otra clase derivada, en este caso la del Desarrollador
class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario, lenguaje_programacion):
        super().__init__(nombre, edad, salario)  # Llamada al constructor de la clase base
        self._lenguaje_programacion = lenguaje_programacion  # Atributo específico de Desarrollador

#Sobrescribo el metodo
    def tipo_empleado(self):
        return "Desarrollador"

#Metodo del lenguaje
    def obtener_lenguaje(self):
        return self._lenguaje_programacion

#Entonces hago uso de esta función para mostrar los datos
def mostrar_informacion_empleado(empleado):
    print(empleado.obtener_informacion())
    print(f"Tipo de empleado: {empleado.tipo_empleado()}")
    if isinstance(empleado, Gerente):
        print(f"Departamento: {empleado.obtener_departamento()}")
    elif isinstance(empleado, Desarrollador):
        print(f"Lenguaje de programación: {empleado.obtener_lenguaje()}")
    print(f"Salario anual: {empleado.calcular_salario_anual()}\n")

#Finalmente uso  instancias de empleados
empleado1 = Empleado("Gabriel Garcia", 21, 400)
gerente1 = Gerente("Ana Luisa Guerra", 33, 1200, "Gerente de ventas")
desarrollador1 = Desarrollador("Luis Sánchez", 28, 1200, "C++")

#Y muestro la información
mostrar_informacion_empleado(empleado1)
mostrar_informacion_empleado(gerente1)
mostrar_informacion_empleado(desarrollador1)
