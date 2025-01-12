# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha: 11/01/2025

#Definicion estructural de "Tarea" y sus cualidades
class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "Pendiente"
#Para afirmar que el trabajo esta hecho
    def marcar_completada(self):
        self.estado = "Completada"
        return f"Tarea '{self.titulo}' completada."
#Sujeto a quien se le asignara las tareas y sus caracteristicas
class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
        self.tareas_asignadas = []

    def asignar_tarea(self, tarea):
        self.tareas_asignadas.append(tarea)

    def completar_tarea(self, tarea):
        tarea.marcar_completada()
        return f"{self.nombre} ha completado la tarea '{tarea.titulo}'."

#Generar el proyecto general donde estara el empleado con sus tareas
class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def ver_progreso(self):
        print(f"\nProgreso del Proyecto '{self.nombre}':")
        for tarea in self.tareas:
            print(f"{tarea.titulo}: {tarea.estado}")

#Aqui pongo el testing del codigo
if __name__ == "__main__":
    # Crear tareas
    tarea1 = Tarea("Desarrollar interfaz de usuario", "Crear la interfaz de usuario")
    tarea2 = Tarea("Base de datos", "Diseñar la base de datos")

#Creo empleados
    empleado1 = Empleado("Samuel", "Desarrollador")
    empleado2 = Empleado("Marta", "Diseñadora")

#Poner tareas a empleados
    empleado1.asignar_tarea(tarea1)
    empleado2.asignar_tarea(tarea2)

#Proyecto y agregar tareas
    proyecto = Proyecto("Aplicación Web")
    proyecto.agregar_tarea(tarea1)
    proyecto.agregar_tarea(tarea2)

#Ver progreso antes de completar tareas
    proyecto.ver_progreso()

#Completar tareas
    print(empleado1.completar_tarea(tarea1))
    print(empleado2.completar_tarea(tarea2))

#Ver progreso después de completar tareas
    proyecto.ver_progreso()