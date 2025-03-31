# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha: 30/03/2025

import tkinter as tk
from tkinter import ttk, messagebox, font
from tkinter.scrolledtext import ScrolledText
import random

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("La Super Lista de Tareas 2077")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f8ff")
#Aqui pongo el estilo personalizado
        self.estilo = ttk.Style()
        self.estilo.theme_use('clam')
        self.estilo.configure('TButton', font=('Helvetica', 10), padding=5)
        self.estilo.configure('TEntry', font=('Helvetica', 12), padding=5)

#Agrego mis fuentes personalizadas
        self.fuente_titulo = font.Font(family='Helvetica', size=16, weight='bold')
        self.fuente_tarea = font.Font(family='Helvetica', size=12)
        self.fuente_tarea_completada = font.Font(family='Helvetica', size=12, overstrike=1)

#los colores
        self.colores = ['#ff9999', '#99ff99', '#9999ff', '#ffff99', '#ff99ff', '#99ffff']

#Configurar
        self.crear_interfaz()

#Lista para tareas
        self.tareas = []

    def crear_interfaz(self):
#principal
        self.frame_principal = tk.Frame(self.root, bg="#f0f8ff", padx=20, pady=20)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

#Título
        self.titulo = tk.Label(
            self.frame_principal,
            text=" Mis Tareas Pendientes ",
            font=self.fuente_titulo,
            bg="#f0f8ff",
            fg="#333366"
        )
        self.titulo.pack(pady=(0, 15))

        self.frame_entrada = tk.Frame(self.frame_principal, bg="#f0f8ff")
        self.frame_entrada.pack(fill=tk.X, pady=(0, 15))
#Campo de entrada
        self.entrada_tarea = ttk.Entry(
            self.frame_entrada,
            width=40,
            style='TEntry'
        )
        self.entrada_tarea.insert(0, "Escribe una nueva tarea...")
        self.entrada_tarea.bind("<FocusIn>", self.limpiar_placeholder)
        self.entrada_tarea.bind("<FocusOut>", self.restaurar_placeholder)
        self.entrada_tarea.bind("<Return>", self.anadir_tarea_evento)
        self.entrada_tarea.pack(side=tk.LEFT, expand=True, fill=tk.X)

#Botón para tarea
        self.boton_anadir = ttk.Button(
            self.frame_entrada,
            text="➕",
            width=3,
            command=self.anadir_tarea
        )
        self.boton_anadir.pack(side=tk.LEFT, padx=(5, 0))

        self.frame_botones = tk.Frame(self.frame_principal, bg="#f0f8ff")
        self.frame_botones.pack(fill=tk.X, pady=(0, 15))

#Botón marcar hecho
        self.boton_completar = ttk.Button(
            self.frame_botones,
            text="Completar",
            command=self.marcar_completada
        )
        self.boton_completar.pack(side=tk.LEFT, expand=True, fill=tk.X)

#Botón eliminar
        self.boton_eliminar = ttk.Button(
            self.frame_botones,
            text="Eliminar",
            command=self.eliminar_tarea
        )
        self.boton_eliminar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

#Botón limpiar
        self.boton_limpiar = ttk.Button(
            self.frame_botones,
            text="Limpiar",
            command=self.limpiar_todas
        )
        self.boton_limpiar.pack(side=tk.LEFT, expand=True, fill=tk.X)

#Lista de tareas
        self.frame_lista = tk.Frame(self.frame_principal, bg="#f0f8ff")
        self.frame_lista.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame_lista)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_tareas = tk.Listbox(
            self.frame_lista,
            yscrollcommand=self.scrollbar.set,
            selectmode=tk.SINGLE,
            bg="white",
            fg="#333333",
            bd=0,
            highlightthickness=0,
            selectbackground="#a6c1ee",
            font=self.fuente_tarea,
            activestyle="none"
        )
        self.lista_tareas.pack(fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.lista_tareas.yview)

#Evento doble click
        self.lista_tareas.bind("<Double-Button-1>", self.marcar_completada_evento)

#Contador tareas
        self.contador_tareas = tk.Label(
            self.frame_principal,
            text="Tareas pendientes: 0",
            bg="#f0f8ff",
            fg="#666666",
            font=('Helvetica', 10)
        )
        self.contador_tareas.pack(pady=(10, 0))

#Efectos
        self.lista_tareas.bind("<Enter>", self.resaltar_lista)
        self.lista_tareas.bind("<Leave>", self.quitar_resaltado)

    def limpiar_placeholder(self, event):
        if self.entrada_tarea.get() == "Escribe una nueva tarea...":
            self.entrada_tarea.delete(0, tk.END)
            self.entrada_tarea.configure(foreground='black')

    def restaurar_placeholder(self, event):
        if not self.entrada_tarea.get():
            self.entrada_tarea.insert(0, "Escribe una nueva tarea...")
            self.entrada_tarea.configure(foreground='grey')

    def resaltar_lista(self, event):
        self.lista_tareas.configure(bg="#f5f5f5")

    def quitar_resaltado(self, event):
        self.lista_tareas.configure(bg="white")

    def anadir_tarea_evento(self, event):
        self.anadir_tarea()

    def anadir_tarea(self):
        tarea = self.entrada_tarea.get().strip()

        if tarea and tarea != "Escribe una nueva tarea...":
#Añadir a la lista interna
            self.tareas.append({"texto": tarea, "completada": False})

#Añadir a la lista
            color = random.choice(self.colores)
            self.lista_tareas.insert(tk.END, tarea)
            self.lista_tareas.itemconfig(tk.END, {'bg': color})
#Limpiar entrada
            self.entrada_tarea.delete(0, tk.END)

#Actualizar contador
            self.actualizar_contador()
        else:
            messagebox.showwarning("Advertencia", "Debes ingresar una tarea válida.")

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]

#Cambiar estado lista
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]

#Cambiar apariencia visual
            if self.tareas[indice]["completada"]:
                self.lista_tareas.itemconfig(indice, {'fg': '#888888', 'font': self.fuente_tarea_completada})
            else:
                self.lista_tareas.itemconfig(indice, {'fg': '#333333', 'font': self.fuente_tarea})
#Actualizar contador
            self.actualizar_contador()
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]

#Eliminar lista interna
            del self.tareas[indice]

#Eliminar lista visual
            self.lista_tareas.delete(indice)

#Actualizar
            self.actualizar_contador()
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")

    def limpiar_todas(self):
        if messagebox.askyesno("Confirmar", "¿Estas seguro de que quieres eliminar todas las tareas?"):
#Limpiar listas
            self.tareas.clear()
            self.lista_tareas.delete(0, tk.END)

#Actualizar contador
            self.actualizar_contador()

    def actualizar_contador(self):
        total = len(self.tareas)
        completadas = sum(1 for tarea in self.tareas if tarea["completada"])
        pendientes = total - completadas

        self.contador_tareas.config(
            text=f"Tareas: {total} totales | {pendientes} pendientes | {completadas} completadas")

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    app.ejecutar()