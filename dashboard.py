"""
Universidad Estatal Amazonica
Nombre: Amir Puente
Fecha de entrega: 02/02/2025
Tema: Adaptación de Proyecto de Programación Orientada a Objetos

"""

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

"""
Decidi modificar el dashboard haciendo uso del famoso tkinter
esto gracias a investigacion personal y horas de practica
"""

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dashboard -Gestión de Proyectos y Tareas")
        self.geometry("600x500")
        self.config(bg="lightblue")
#Aqui van los proyectos y tareas
        self.proyectos ={}  #Diccionario
#Interfaz
        self.create_widgets()

    def create_widgets(self):
#Pongo el titulo
        self.label_titulo = tk.Label(self, text="Mis Proyectos y Tareas", font=("Helvetica", 20), bg="lightblue")
        self.label_titulo.pack(pady=10)
#Lista de proyectos
        self.proyectos_frame = tk.Frame(self)
        self.proyectos_frame.pack(pady=10)

        self.listbox_proyectos = tk.Listbox(self.proyectos_frame, height=8, width=50, font=("Helvetica", 14))
        self.listbox_proyectos.grid(row=0, column=0, padx=10)

#Agregar el proyecto
        self.button_agregar_proyecto = tk.Button(self, text="Agregar Proyecto", font=("Helvetica", 14), bg="green",
                                                 fg="white", command=self.agregar_proyecto)
        self.button_agregar_proyecto.pack(pady=5)
#Ver tareas
        self.button_ver_tareas = tk.Button(self, text="Ver Tareas", font=("Helvetica", 14), bg="blue", fg="white",
                                           command=self.ver_tareas)
        self.button_ver_tareas.pack(pady=5)
#Eliminar proyecto
        self.button_eliminar_proyecto = tk.Button(self, text="Eliminar Proyecto", font=("Helvetica", 14), bg="red",
                                                  fg="white", command=self.eliminar_proyecto)
        self.button_eliminar_proyecto.pack(pady=5)

    def agregar_proyecto(self):
#Pido el nombre del trabajo
        nombre_proyecto = simpledialog.askstring("Nuevo Proyecto", "Digita el nombre del proyecto:")
        if nombre_proyecto:
            if nombre_proyecto not in self.proyectos:
                self.proyectos[nombre_proyecto] = []  #Proyecto con lista vacía de tareas
                self.listbox_proyectos.insert(tk.END, nombre_proyecto)
            else:
                messagebox.showwarning("Ponte pilas", "El proyecto ya existe")

    def ver_tareas(self):
#Obtener el proyecto
        seleccion = self.listbox_proyectos.curselection()
        if seleccion:
            proyecto_seleccionado = self.listbox_proyectos.get(seleccion)
            self.ventana_tareas(proyecto_seleccionado)
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona un proyecto")

    def ventana_tareas(self, proyecto):
#Creo una ventana secundaria para ver las tareas
        ventana_tareas = tk.Toplevel(self)
        ventana_tareas.title(f"Tareas de {proyecto}")
        ventana_tareas.geometry("500x400")

        label_tareas = tk.Label(ventana_tareas, text=f"Tareas en el Proyecto '{proyecto}'", font=("Helvetica", 14))
        label_tareas.pack(pady=10)

        listbox_tareas = tk.Listbox(ventana_tareas, height=10, width=50, font=("Helvetica", 12))
        listbox_tareas.pack(pady=10)

#Mostrar las tareas
        for tarea in self.proyectos[proyecto]:
            listbox_tareas.insert(tk.END, tarea[0])

#Entradas y botones para tareas
        frame_tareas = tk.Frame(ventana_tareas)
        frame_tareas.pack(pady=10)

        entry_tarea = tk.Entry(frame_tareas, font=("Helvetica", 12), width=30)
        entry_tarea.grid(row=0, column=0, padx=10)

        entry_fecha = tk.Entry(frame_tareas, font=("Helvetica", 12), width=15)
        entry_fecha.grid(row=0, column=1, padx=10)

        def agregar_tarea():
            tarea_nombre = entry_tarea.get()
            tarea_fecha = entry_fecha.get()

#Sirve para validar la fecha
            try:
                fecha = datetime.strptime(tarea_fecha, "%Y-%m-%d")
            except ValueError:
                messagebox.showwarning("Error de Fecha", "La fecha debe estar en formato YYYY-MM-DD.")
                return
            if tarea_nombre != "" and tarea_fecha != "":
                self.proyectos[proyecto].append((tarea_nombre, fecha))
                listbox_tareas.insert(tk.END, tarea_nombre)
                entry_tarea.delete(0, tk.END)
                entry_fecha.delete(0, tk.END)
            else:
                messagebox.showwarning("Advertencia", "Debes ingresar un nombre y una fecha para la tarea")

        button_agregar_tarea = tk.Button(ventana_tareas, text="Agregar Tarea", font=("Helvetica", 12), bg="green",
                                         fg="white", command=agregar_tarea)
        button_agregar_tarea.pack(pady=5)

    def eliminar_proyecto(self):
        seleccion = self.listbox_proyectos.curselection()
        if seleccion:
            proyecto_seleccionado = self.listbox_proyectos.get(seleccion)
            del self.proyectos[proyecto_seleccionado]
            self.listbox_proyectos.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", "Debes seleccionar un proyecto para eliminar")

#Finalmente pruebo
if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
