# "Universidad Estatal Amazonica"
# Clase: POO Paralelo A
# Nombre: Amir Puente
# Fecha: 11/01/2025

#Crear y definir la clase libro con sus respectivas caracteristicas
class Libro:
    def __init__(self, titulo, autor, isbn, fecha_publicacion):
        self.titulo =titulo
        self.autor =autor
        self.isbn =isbn
        self.fecha_publicacion =fecha_publicacion
        self.disponible =True

#Defino la opcion de prestar el libro
    def prestar(self):
        if self.disponible:
            self.disponible =False
            return f"El libro '{self.titulo}' se presto correctamente"
        else:
            return f"El libro '{self.titulo}' de momento no está disponible"
#Defino la opcion para devolver el libro
    def devolver(self):
        self.disponible = True
        return f"El libro '{self.titulo}' se ha devuelto"
#Aqui va la clasificacion del usuario
class Usuario:
    def __init__(self, nombre, email):
        self.nombre =nombre
        self.email =email
        self.libros_prestados =[]
#Funcionalidad para solicitar el libro si esta disponible
    def solicitar_libro(self, libro):
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
            return f"{self.nombre} requiere el libro '{libro.titulo}'"
        else:
            return f"El libro '{libro.titulo}' no está disponible para prestar"
#Aqui para devolver
    def devolver_libro(self, libro):
        libro.devolver()
        self.libros_prestados.remove(libro)
        return f"{self.nombre} devolvio el libro '{libro.titulo}'"
#La biblioteca donde se almacenan los libros y usuarios registrados
class Biblioteca:
    def __init__(self):
        self.catalogo_libros =[]
        self.usuarios =[]
#Sirve para añadir libros al catalogo
    def agregar_libro(self, libro):
        self.catalogo_libros.append(libro)

    def ver_catalogo(self):
        print("\nCatalogo de Libros:")
        for libro in self.catalogo_libros:
            disponibilidad = 'Esta disponible' if libro.disponible else 'No esta disponible'
            print(f"{libro.titulo} - {disponibilidad}")

#Probar el sistema de biblioteca
if __name__ == "__main__":
    #Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "93462", "1967")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "44279", "1605")
#Creao usuarios ficticios
    usuario1 = Usuario("Mateo Naveda", "matnav2002@gmail.com")
    usuario2 = Usuario("Arely Pesantes", "arelyyp99@outlook.com")

#Genero la biblioteca y agrego libros
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

#Ver
    biblioteca.ver_catalogo()

#Prestar
    print(usuario1.solicitar_libro(libro1))
    print(usuario2.solicitar_libro(libro2))

#Mostrar catálogo después de prestar los libros
    biblioteca.ver_catalogo()

#Devolver libros
    print(usuario1.devolver_libro(libro1))
    print(usuario2.devolver_libro(libro2))

#Mostrar catálogo después de devoluciones
    biblioteca.ver_catalogo()