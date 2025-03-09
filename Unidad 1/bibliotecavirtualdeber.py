# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha: 08/03/2025

#clase libro con sus respectivas caracteristicas
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  #Tupla título/autor
        self.categoria = categoria
        self.isbn = isbn
#libro, autor, categoria, isbn
    def __str__(self):
        return f"Libro: {self.titulo_autor[0]} by {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"
#base usuario para los demas
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  #Libros prestados
#igual que el anterior
    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"
#biblioteca con directrices requeridas
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  #libros disponibles
        self.usuarios_registrados = set()  #IDs de usuarios
        self.usuarios = {}  #Diccionario de usuarios
#agregar
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Muy bien, el libro '{libro.titulo_autor[0]}' se ha añadido.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")
#eliminar
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Genial, has eliminado el libro con ISBN {isbn}.")
        else:
            print(f"El libro con ISBN {isbn} no existe en la biblioteca.")
#nuevos usuarios
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Perfecto, el usuario '{usuario.nombre}' se ha añadido correctamente.")
        else:
            print(f"Error, el usuario con ID {usuario.id_usuario} ya está registrado.")
#dar de baja
    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja correctamente.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")
#prestar y como lo realiza
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles[isbn]
            usuario.libros_prestados.append(libro)
            del self.libros_disponibles[isbn]
            print(f"El libro '{libro.titulo_autor[0]}' fue prestado a '{usuario.nombre}'.")
        else:
            print("Usuario o libro no encontrado")
#devolver y como lo hace
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Perfecto, el libro '{libro.titulo_autor[0]}' ha sido devuelto por '{usuario.nombre}'.")
                    return
            print(f"El libro con ISBN {isbn} no ha sido prestado a este usuario")
        else:
            print(f"Error, usuario con ID {id_usuario} no está registrado.")
#buscar libros titulo
    def buscar_libro_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.titulo_autor[0] == titulo]
        return resultados
#buscar libros autor
    def buscar_libro_por_autor(self, autor):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.titulo_autor[1] == autor]
        return resultados
#buscar libros categoria
    def buscar_libro_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.categoria == categoria]
        return resultados
#libros prestados
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return []
#menu final
def mostrar_menu():
    print("\n--------- La Super Biblioteca Multiversal ---------")
    print("1. Registrar usuario")
    print("2. Añadir libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro por título")
    print("6. Buscar libro por autor")
    print("7. Buscar libro por categoría")
    print("8. Listar libros prestados")
    print("9. Dar de baja usuario")
    print("10. Quitar Libro")
    print("11. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "2":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)

        elif opcion == "3":
            id_usuario = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "4":
            id_usuario = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "5":
            titulo = input("Ingrese el título del libro: ")
            resultados = biblioteca.buscar_libro_por_titulo(titulo)
            for libro in resultados:
                print(libro)

        elif opcion == "6":
            autor = input("Ingrese el autor del libro: ")
            resultados = biblioteca.buscar_libro_por_autor(autor)
            for libro in resultados:
                print(libro)

        elif opcion == "7":
            categoria = input("Ingrese la categoría del libro: ")
            resultados = biblioteca.buscar_libro_por_categoria(categoria)
            for libro in resultados:
                print(libro)

        elif opcion == "8":
            id_usuario = input("Ingrese el ID del usuario: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            for libro in libros_prestados:
                print(libro)

        elif opcion == "9":
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.dar_de_baja_usuario(id_usuario)

        elif opcion == "10":
            isbn = input("Ingrese el ISBN del libro: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "11":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()