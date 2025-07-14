# Clase Libro: representa un libro en una biblioteca
class Libro:
    def __init__(self, titulo, autor):
        # Constructor: se llama automáticamente al crear un objeto de la clase
        self.titulo = titulo
        self.autor = autor
        print(f"[Constructor] Se ha creado el libro: '{self.titulo}' de {self.autor}")

    def mostrar_info(self):
        print(f"Título: {self.titulo} | Autor: {self.autor}")

    def __del__(self):
        # Destructor: se llama automáticamente cuando el objeto es destruido
        print(f"[Destructor] Se ha eliminado el libro: '{self.titulo}'")

# Clase Biblioteca: gestiona una colección de libros
class Biblioteca:
    def __init__(self):
        self.libros = []
        print("[Constructor] Biblioteca inicializada vacía.")

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def mostrar_biblioteca(self):
        print("\n📚 Lista de libros en la biblioteca:")
        for libro in self.libros:
            libro.mostrar_info()

    def __del__(self):
        print("[Destructor] Cerrando la biblioteca y eliminando libros...")
        for libro in self.libros:
            del libro
        self.libros = []
        print("Biblioteca cerrada.")

# Bloque principal para ejecutar el programa
if __name__ == "__main__":
    # Crear biblioteca
    mi_biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("1984", "George Orwell")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")

    # Agregar libros a la biblioteca
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)

    # Mostrar libros
    mi_biblioteca.mostrar_biblioteca()

    # Eliminar biblioteca (también eliminará los libros)
    del mi_biblioteca
