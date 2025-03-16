#"Universidad Estatal Amazonica"
#Clase: POO Paralelo A
#Nombre: Amir Puente
#Fecha de entrega: 16/03/2025

#De manera general es un pequeño conversor de divisas
#Convierte dolares a francos suizos

import tkinter as tk
from tkinter import ttk, messagebox
#Aqui coloco la tasa de conversión de 0.92 francos suizos
TASA_CONVERSION = 0.92

#Esta es la función principal
def convertir():
    try:
        dolares = float(entrada_dolares.get()) #valor digitado
        francos = dolares * TASA_CONVERSION    #convertirlo
        resultado = f"{dolares} USD = {francos:.2f} CHF"
        lista_resultados.insert(0, resultado)  #añadir a lista
        entrada_dolares.delete(0, tk.END)     #limpiar
    except ValueError:
        messagebox.showerror("Error", "Debes digitar un valor numérico válido.")

#Aqui va la función para limpiar
def limpiar():
    lista_resultados.delete(0, tk.END)

#ventana inicial
ventana = tk.Tk()
ventana.title("El SuperConversor de Dólares a Francos Suizos")

#Creo los widgets
etiqueta_instruccion = ttk.Label(ventana, text="Digita la cantidad en dólares (USD):")
etiqueta_instruccion.grid(row=0, column=0, padx=10, pady=10)

entrada_dolares = ttk.Entry(ventana, width=20)
entrada_dolares.grid(row=0, column=1, padx=10, pady=10)

boton_convertir = ttk.Button(ventana, text="Convertirlo", command=convertir)
boton_convertir.grid(row=0, column=2, padx=10, pady=10)

lista_resultados = tk.Listbox(ventana, width=40, height=10)
lista_resultados.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=2, column=1, padx=10, pady=10)

#Iniciar el bucle principal
ventana.mainloop()