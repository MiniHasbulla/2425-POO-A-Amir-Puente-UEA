#"Universidad Estatal Amazonica"
#Clase: POO Paralelo A
#Nombre: Amir Puente
#Fecha de entrega:26/01/2025
"""
Programa que inicializa archivos,
simula la creacion de contenido,
y finalmente los destruye
import os
"""
class Archivo:
    def __init__(self, nombre, extension, contenido):
#Constructor que inicializa
        self.nombre =nombre
        self.extension =extension
        self.contenido =contenido
        self.ruta = f"{self.nombre}.{self.extension}"
        print(f"El siguiente archivo ha sido creado: {self.ruta}")

    def escribir_contenido(self):
#Esto para simular contenido en el archivo
        print(f"Escribiendo en {self.ruta}: {self.contenido}")

    def __del__(self):
#Destructor-el cierre del archivo.
        print(f"El archivo {self.ruta} se cerro y los recursos fueron liberados")

class Carpeta:
    def __init__(self, nombre):
#Constructor carpeta
        self.nombre = nombre
        self.archivos = []
        print(f"La siguiente carpeta se creo: {self.nombre}")

    def agregar_archivo(self, archivo):
#Añadir un archivo
        self.archivos.append(archivo)
        print(f"El archivo {archivo.ruta} se agrego a la carpeta {self.nombre}")

    def __del__(self):
#Destructor que limpia los archivos dentro de la carpeta.
        for archivo in self.archivos:
            del archivo  # Llama a __del__ de cada archivo
        print(f"La carpeta {self.nombre} se elimino satisfactoriamente y sus archivos han cerrado.")

#Probando el codigo
mi_carpeta =Carpeta("Documentos Finales UEA")
#Creando archivos
archivo1 =Archivo("Fisica2", "txt", "Realizar el Practico Experimental 2")
archivo2 =Archivo("Estadistica", "txt", "Completar las asignaciones de la semana")
mi_carpeta.agregar_archivo(archivo1)
mi_carpeta.agregar_archivo(archivo2)

#Escribiendo
archivo1.escribir_contenido()
archivo2.escribir_contenido()
