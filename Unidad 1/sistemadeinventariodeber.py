# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha de entrega:16/02/2025

#Defino la clase producto con sus respectivas caracteristicas
#Siguiendo lo pedido en el enunciado
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id =id
        self.nombre =nombre
        self.cantidad =cantidad
        self.precio =precio

#Coloco set/get de cada uno
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad =cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio =precio
#Ahora continuo con la clase "Inventario"
#En esta añado los productos que se colocaran
#Asi mismo coloco ciertas restricciones logicas para el registro de los productos
class Inventario:
    def __init__(self):
        self.productos =[]

#Agrego los productos, si este producto ya esta registrado no se puede volver a agregar
    def anadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("El numero del producto se encuentra duplicado, no se puede añadir.")
                return
        self.productos.append(producto)
        print(f"El producto '{producto.get_nombre()}' ha sido añadido satisfactoriamente")

#Ahora defino la funcion de eliminar un producto previamente registrado
    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print(f"El producto con numero '{id}' ha sido eliminado")
                return
        print(f"El producto con numero '{id}' no se ha localizado")

#En este caso coloco la funcion requerida para modificar un producto ya registrado
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print(f"El producto '{id}' fue modificado")
                return
        print(f"El producto numero '{id}' no pudo ser encontrado")

#Ahora coloco la funcion que me permitira buscar los productos en el inventario
    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("Productos encontrados:")
            for p in resultados:
                print(f"Numero: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("No se han encontraron productos con este nombre")

#Indicar/verificar los productos
    def mostrar_productos(self):
        if not self.productos:
            print("No se han registrado productos en el inventario")
        else:
            print("Inventario de productos:")
            for p in self.productos:
                print(f"Numero: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")

#Una vez cimentado las bases de la funcionalidad del sistema continuo con el menu
def menu():
    inventario = Inventario()
    opciones = {
        '1': "Agrega un nuevo producto",
        '2': "Elimina un producto mediante su numero",
        '3': "Actualiza la cantidad o precio de un producto por su numero",
        '4': "Buscar productos por nombre",
        '5': "Mostrar todos los productos en el inventario",
        '6': "Salir"
    }
    while True:
        print("\n¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥")
        print("Bienvenid@ al Gestor3000")
        print("¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥")
        for clave, valor in opciones.items():
            print(f"{clave}. {valor}")
        eleccion = input("Para continuar escoge una opción: ")
        if eleccion == '1':
            id= input("Digita el numero del producto: ")
            nombre= input("Escribe el nombre del producto: ")
            cantidad= int(input("Digita la cantidad del producto: "))
            precio= float(input("Escribe el precio del producto: "))
            producto= Producto(id, nombre, cantidad, precio)
            inventario.anadir_producto(producto)
        elif eleccion == '2':
            id = input("Digita el numero del producto que deseas eliminar: ")
            inventario.eliminar_producto(id)
        elif eleccion == '3':
            id = input("Escribe el numero del producto para actualizar: ")
            cantidad = input("Introduce la nueva cantidad (deja en blanco si no deseas cambiarla): ")
            precio = input("Redacta el nuevo precio (deja en blanco si no deseas cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif eleccion == '4':
            nombre = input("Digita el nombre del producto que buscas: ")
            inventario.buscar_producto(nombre)
        elif eleccion == '5':
            inventario.mostrar_productos()
        elif eleccion == '6':
            print("Saliendo del Gestor3000...........")
            break
        else:
            print("La opción que digitaste no es válida. Selecciona una opción del menú")

if __name__ == "__main__":
    menu()