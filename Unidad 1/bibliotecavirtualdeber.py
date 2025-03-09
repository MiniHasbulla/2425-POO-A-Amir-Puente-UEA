# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha: 08/03/2025

#defino las caracteristicas para los libros
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  #Tupla para título/autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.titulo_autor[0]} by {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"
#ahora la clase usuario con sus definciones
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  #Libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"

#de manera similar a los anteriores pero con la biblioteca en general
#aqui aplico y continuo con las directrices del proyecto
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  #Diccionario libros disponibles
        self.usuarios_registrados = set()  #IDs de usuarios únicos
        self.usuarios = {}  #Diccionario de usuarios
#me permite agregar un libro a la biblioteca
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Muy bien, el libro '{libro.titulo_autor[0]}' se ha añadido.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")
#eliminar los libros
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Genial, has eliminado el libro con ISBN {isbn}.")
        else:
            print(f"El libro con ISBN {isbn} no existe en la biblioteca.")
#agregar usuarios
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Perfecto, el usuario '{usuario.nombre}' se ha añadido correctamente.")
        else:
            print(f"Error, el usuario con ID {usuario.id_usuario} ya está registrado.")
#dar de baja a determinado usuario
    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja correctamente.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")
#esto me ayudara con prestar los libros
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles[isbn]
            usuario.libros_prestados.append(libro)
            del self.libros_disponibles[isbn]
            print(f"El libro '{libro.titulo_autor[0]}' fue prestado a '{usuario.nombre}'.")
        else:
            print("Usuario o libro no encontrado")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Perfercto, el libro '{libro.titulo_autor[0]}' ha sido devuelto por '{usuario.nombre}'.")
                    return
            print(f"El libro con ISBN {isbn} no ha sido prestado a este usuario")
        else:
            print(f"Error, usuario con ID {id_usuario} no está registrado.")

    def buscar_libro_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.titulo_autor[0] == titulo]
        return resultados

    def buscar_libro_por_autor(self, autor):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.titulo_autor[1] == autor]
        return resultados

    def buscar_libro_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.categoria == categoria]
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return []

#Ejemplificacion del codigo
if __name__ == "__main__":
    biblioteca = Biblioteca()
    #redacto los libros
    libro1 = Libro("The Stand", "Stephen King", "Terror Postapocaliptico", "978-0307743688")
    libro2 = Libro("Fahrenheit 451", "Ray Bradbury", "Literatura Distopica", "978-6070764004")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    #agrego usuarios
    usuario1 = Usuario("Santino Gomez", 1)
    usuario2 = Usuario("Daniel Silva", 2)
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    #prestar libros
    biblioteca.prestar_libro(1, "978-0307743688")
    biblioteca.prestar_libro(2, "978-6070764004")

    #libros prestados
    print("\nLibros prestados a Santino Gomez:")
    for libro in biblioteca.listar_libros_prestados(1):
        print(libro)

    #devolver libros
    biblioteca.devolver_libro(1, "978-0307743688")
    #buscar libros
    print("\nBuscar libros de Literatura Distopica:")
    for libro in biblioteca.buscar_libro_por_categoria("Literatura Distopica"):
        print(libro)