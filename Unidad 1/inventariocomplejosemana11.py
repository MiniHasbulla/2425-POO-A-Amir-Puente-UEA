# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha: 02/03/2025

#para la serialización de los objetos
import pickle
#clase inicial con caracteristicas definidas
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id =id
        self.nombre =nombre
        self.cantidad =cantidad
        self.precio =precio
#definir cada uno
    def obtener_id(self):
        return self.id
    def obtener_nombre(self):
        return self.nombre
    def obtener_cantidad(self):
        return self.cantidad
    def obtener_precio(self):
        return self.precio
    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad
    def establecer_precio(self, precio):
        self.precio = precio
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"
#segunda clase mas importante, el inventario
class Inventario:
    def __init__(self):
        self.productos = {}
#definir como se agregan los productos
    def agregar_producto(self, producto):
        if producto.id not in self.productos:
            self.productos[producto.id] = producto
            print(f"El item {producto.nombre} fue añadido")
        else:
            print(f"Error, ya existe un producto con este ID {producto.id}.")
#para eliminar el producto y que mensaje saltara
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"El item con ID {id_producto} fue eliminado")
        else:
            print(f"Error, no existe un producto con el ID {id_producto}")
#para modificar un producto previo
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            print(f"El item con ID {id_producto} se ha actualizado")
        else:
            print(f"Error, no existe el producto con ID {id_producto}")
#para realizar la busqueda
    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        if resultados:
            print("Resultados obtenidos:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con este nombre")
#para indicar el inventario
    def mostrar_inventario(self):
        if self.productos:
            print("He aqui el inventario:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está completamente vacio")

def guardar_inventario(inventario, nombre_archivo="inventario.pkl"):
    with open(nombre_archivo, "wb") as archivo:
        pickle.dump(inventario.productos, archivo)
    print("Se ha guardado completamente")

def cargar_inventario(nombre_archivo="inventario.pkl"):
    try:
        with open(nombre_archivo, "rb") as archivo:
            productos = pickle.load(archivo)
            inventario = Inventario()
            inventario.productos = productos
            print("Inventario cargado al 100%")
            return inventario
    except FileNotFoundError:
        print("No se encontró el archivo de inventario, creando uno")
        return Inventario()

def mostrar_menu():
    print("\n[[[[[[[[[[[[ El Inventanetor 2077 ]]]]]]]]]]]]]]")
    print("1. Añadir Producto                         ]]]]]")
    print("2. Eliminar Producto                       ]]]]]")
    print("3. Actualizar Producto                     ]]]]]")
    print("4. Buscar Producto por Nombre              ]]]]]")
    print("5. Mostrar Inventario                      ]]]]]")
    print("6. Guardar Inventario                      ]]]]]")
    print("7. Cargar Inventario                       ]]]]]")
    print("8. Salir                                   ]]]]]")
    print("[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]")

def ejecutar_menu():
    inventario = cargar_inventario()

    while True:
        mostrar_menu()
        opcion = input("\nEscoge la opcion requerida ").strip().lower()

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad (o 0 para no cambiar): "))
            precio = float(input("Nuevo precio (o 0.0 para no cambiar): "))
            inventario.actualizar_producto(id_producto, cantidad if cantidad != 0 else None, precio if precio != 0.0 else None)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == "5":
            inventario.mostrar_inventario()
        elif opcion == "6":
            guardar_inventario(inventario)
        elif opcion == "7":
            inventario = cargar_inventario()
        elif opcion == "8":
            print("¡Hasta la vista baby!")
            break

        else:
            print("Opción no válida. Debes seleccionar una opción válida")

# Ejecutar el programa
if __name__ == "__main__":
    ejecutar_menu()
