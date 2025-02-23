# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha de entrega:16/02/2025

#Defino la clase producto con sus respectivas caracteristicas
#Siguiendo lo pedido en el enunciado
import os
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id =id
        self.nombre =nombre
        self.cantidad =cantidad
        self.precio =precio

    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_string(line):
        id, nombre, cantidad, precio = line.strip().split(',')
        return Producto(id, nombre, int(cantidad), float(precio))

class Inventario:
    ARCHIVO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as f:
                for producto in self.productos:
                    f.write(str(producto) + "\n")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO):
            return
        try:
            with open(self.ARCHIVO, "r") as f:
                self.productos = [Producto.from_string(line) for line in f]
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def anadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("El número del producto ya existe por ello no se puede añadir")
            return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print(f"El producto '{producto.nombre}' se añadio correctamente.")

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print(f"El producto '{id}' se elimino")
                return
        print(f"No se encontró el producto '{id}'")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_en_archivo()
                print(f"El producto '{id}' fue actualizado")
                return
        print(f"No se encontró el producto '{id}'")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            print("Productos:")
            for p in resultados:
                print(f"Número: {p.id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        else:
            print("No se han encontraron productos con este nombre")

    def mostrar_productos(self):
        if not self.productos:
            print("No existen productos en el inventario")
        else:
            print("Inventario:")
            for p in self.productos:
                print(f"Número: {p.id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")

def menu():
    inventario = Inventario()
    opciones = {
        '1': "Agregar productos",
        '2': "Eliminar productos por número",
        '3': "Actualizar cantidad o precio de un producto",
        '4': "Buscar productos por nombre",
        '5': "Mostrar todos los productos",
        '6': "Salir"
    }

    while True:
        print("\n¥¥¥¥¥¥¥¥¥¥ El SuperGestor3000 ¥¥¥¥¥¥¥¥¥¥")
        for clave, valor in opciones.items():
            print(f"{clave}. {valor}")
        eleccion = input("Selecciona: ")

        if eleccion == '1':
            id = input("Número: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.anadir_producto(Producto(id, nombre, cantidad, precio))
            except ValueError:
                print("Error: Por favor digita valores válidos")

        elif eleccion == '2':
            id = input("Número del producto para eliminar: ")
            inventario.eliminar_producto(id)

        elif eleccion == '3':
            id = input("Número del producto para actualizarlo: ")
            cantidad = input("Nueva cantidad (si no cambia dejar en blanco): ")
            precio = input("Nuevo precio (si no cambia dejar en blanco): ")
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("Error, debes digitar numeros válidos")

        elif eleccion == '4':
            nombre = input("Nombre del producto para buscar: ")
            inventario.buscar_producto(nombre)

        elif eleccion == '5':
            inventario.mostrar_productos()

        elif eleccion == '6':
            print("Saliendo del SuperGestor3000.........")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()