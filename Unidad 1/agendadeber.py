# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha: 23/03/2025

#librerias requeridas
#tkinter, el messagebox y tambien instale el tkcalendar
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

#clase principal, defino los marcos y el nombre
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SuperAgenda Personal 2077")
        self.root.geometry("600x400")

#Aqui van los contenedores principales
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(fill=tk.X, padx=10, pady=5)

        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(fill=tk.X, padx=10, pady=5)

#treeview con cada uno de los parametros
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

#entrada para digitacion
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entrada, date_pattern="yyyy-mm-dd")
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(self.frame_entrada, width=30)
        self.descripcion_entry.grid(row=0, column=5, padx=5, pady=5)

#aqui van los botones con su respectiva funcionalidad
        self.boton_agregar = tk.Button(self.frame_botones, text="Añade un Evento", command=self.agregar_evento)
        self.boton_agregar.pack(side=tk.LEFT, padx=5)

        self.boton_eliminar = tk.Button(self.frame_botones, text="Elimina el Evento seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.pack(side=tk.LEFT, padx=5)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=root.quit)
        self.boton_salir.pack(side=tk.RIGHT, padx=5)

#añadir eventos
    def agregar_evento(self):

#consigue los valores digitados
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

#Ver que este lleno correctamente
        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos Vacíos", "Para continuar llena todos los campos")
            return

#añadir el evento al treeview
        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))

#limpiar
        self.fecha_entry.set_date(None)
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
#resaltar la seleccion
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Nada Seleccionado", "Debes seleccionar un evento para eliminar")
            return
#confirmacion
        confirmar = messagebox.askyesno("Confirmas eliminarlo", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmar:
            self.tree.delete(seleccionado)

#iniciar
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()