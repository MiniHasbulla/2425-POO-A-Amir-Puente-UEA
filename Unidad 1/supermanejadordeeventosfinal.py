# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha: 06/04/2025

#librerias requeridas
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

#clases principales en este caso la super aplicacion mejorada
class ImprovedTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ColorTask Pro - Superlista de Tareas Mejorada")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

#Configuro estilo
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", padding=6, relief="flat", background="#4a6fa5", foreground="white")
        self.style.map("TButton", background=[("active", "#3a5a80")])

#Fuentes especificas
        self.title_font = Font(family="Helvetica", size=16, weight="bold")
        self.task_font = Font(family="Helvetica", size=12)
        self.completed_font = Font(family="Helvetica", size=12, overstrike=1)

#luego coloco las variables
        self.tasks = []
        self.category_colors = {
            "Personal": "#FF9AA2",
            "Trabajo": "#FFB7B2",
            "Estudio": "#FFDAC1",
            "Hogar": "#E2F0CB",
            "Otros": "#B5EAD7"
        }

        self.setup_ui()
        self.setup_keyboard_shortcuts()

    def setup_ui(self):
#aqui va el frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

#primero el titulo
        title_label = tk.Label(main_frame, text="ColorTask Pro", font=self.title_font,
                               bg="#f0f0f0", fg="#4a6fa5")
        title_label.pack(pady=(0, 20))

#frame
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 20))

#el campo de entrada
        self.task_entry = ttk.Entry(input_frame, font=self.task_font)
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.task_entry.focus()

#las categoría
        self.category_var = tk.StringVar(value="Personal")
        category_menu = ttk.OptionMenu(input_frame, self.category_var, "Personal", *self.category_colors.keys())
        category_menu.pack(side=tk.LEFT, padx=(0, 10))

#aqui va el añadir
        add_button = ttk.Button(input_frame, text="➕ Añadir (Enter)", command=self.add_task)
        add_button.pack(side=tk.LEFT)

#Frame de tareas
        tasks_frame = ttk.Frame(main_frame)
        tasks_frame.pack(fill=tk.BOTH, expand=True)

#lista de tareas
        self.canvas = tk.Canvas(tasks_frame, bg="#f0f0f0", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(tasks_frame, orient="vertical", command=self.canvas.yview)
        self.tasks_container = ttk.Frame(self.canvas)

        self.tasks_container.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.tasks_container, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#frame controles
        controls_frame = ttk.Frame(main_frame)
        controls_frame.pack(fill=tk.X, pady=(20, 0))
#los botones
        complete_button = ttk.Button(controls_frame, text="Completar (Ctrl+C)", command=self.complete_selected)
        complete_button.pack(side=tk.LEFT, padx=(0, 10))

        delete_button = ttk.Button(controls_frame, text="Eliminar (Ctrl+D)", command=self.delete_selected)
        delete_button.pack(side=tk.LEFT)
#Informacion para los usuarios
        shortcuts_label = tk.Label(controls_frame,
                                   text="Atajos: Enter=Añadir | Ctrl+C=Completar | Ctrl+D=Eliminar | Esc=Salir",
                                   bg="#f0f0f0", fg="#666")
        shortcuts_label.pack(side=tk.RIGHT)

    def setup_keyboard_shortcuts(self):
#va para que cuando se ponga enter solo funciona en el campo de entrada
        self.task_entry.bind("<Return>", lambda e: self.add_task())

#los atajos con Ctrl
        self.root.bind("<Control-c>", lambda e: self.complete_selected())
        self.root.bind("<Control-d>", lambda e: self.delete_selected())
        self.root.bind("<Escape>", lambda e: self.root.quit())

#este es importante ya que deshabilita los atajos cuando el campo de entrada
        self.task_entry.bind("<FocusIn>", self.disable_global_shortcuts)
        self.task_entry.bind("<FocusOut>", self.enable_global_shortcuts)

    def disable_global_shortcuts(self, event):
#Deshabilitar cuando se está escribiendo
        self.root.unbind("<Control-c>")
        self.root.unbind("<Control-d>")

    def enable_global_shortcuts(self, event):
#habilitar cuando no se está escribiendo
        self.root.bind("<Control-c>", lambda e: self.complete_selected())
        self.root.bind("<Control-d>", lambda e: self.delete_selected())

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            category = self.category_var.get()
            task_id = len(self.tasks) + 1
            task_data = {
                "id": task_id,
                "text": task_text,
                "completed": False,
                "category": category,
                "color": self.category_colors[category]
            }
            self.tasks.append(task_data)
            self.render_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Ponte pilas", "Debes ingresar una tarea")

    def render_tasks(self):
#limpiar tareas existentes
        for widget in self.tasks_container.winfo_children():
            widget.destroy()

        for task in self.tasks:
            task_frame = tk.Frame(
                self.tasks_container,
                bg=task["color"],
                padx=10,
                pady=8,
                highlightthickness=0,
                bd=0,
                relief=tk.RAISED
            )
            task_frame.pack(fill=tk.X, pady=5, ipadx=5, ipady=5)

            var = tk.BooleanVar(value=task["completed"])
            checkbox = tk.Checkbutton(
                task_frame,
                variable=var,
                command=lambda t=task: self.toggle_task(t),
                bg=task["color"],
                activebackground=task["color"]
            )
            checkbox.pack(side=tk.LEFT)

            task_text = tk.Label(
                task_frame,
                text=task["text"],
                font=self.completed_font if task["completed"] else self.task_font,
                bg=task["color"],
                fg="#555" if task["completed"] else "#333",
                wraplength=600,
                justify=tk.LEFT
            )
            task_text.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))

#Categorias especificas dependiendo del tema
            category_label = tk.Label(
                task_frame,
                text=task["category"],
                font=("Helvetica", 10, "italic"),
                bg=task["color"],
                fg="#555"
            )
            category_label.pack(side=tk.RIGHT, padx=(0, 10))

#Estilo para tareas
            if task["completed"]:
                task_frame.config(relief=tk.SUNKEN)
                for child in task_frame.winfo_children():
                    if isinstance(child, tk.Label):
                        child.config(fg="#888")

    def toggle_task(self, task):
        task["completed"] = not task["completed"]
        self.render_tasks()

#Efecto al completar
        if task["completed"]:
            self.root.after(100, lambda: self.root.bell()) #agregue este sonido

    def complete_selected(self):
        for task in self.tasks:
            if not task["completed"]:
                self.toggle_task(task)
                break
        else:
            messagebox.showinfo("Info", "Todas las tareas están completadas")

    def delete_selected(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No hay tareas para eliminar")
            return

        self.tasks.pop()
        self.render_tasks()
#efecto visual
        self.root.after(100, lambda: self.root.bell())


if __name__ == "__main__":
    root = tk.Tk()
    app = ImprovedTodoApp(root)
    root.mainloop()