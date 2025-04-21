class Libreria:
    def __init__(self,nombre_libros,paginas_libro,autor_libro):
        self.nombre_libros = nombre_libros
        self.paginas_libro = paginas_libro
        self.autor_libro = autor_libro
    def libros(self):
        print(input(f"El libro llamado {self.nombre_libros} ha sido guardado exitosamente"))
    def paginas(self):
        print(int(input(f"El libro llamado {self.nombre_libros} tiene una cantidad de paginas de {self.paginas_libro}")))
    def autor(self):
        print(input(f"El libro llamado {self.nombre_libros} su autor es {self.autor_libro}"))
class Estanteria:
    def __init__(self,num_estante,tipo_obra):
        self.num_estante = num_estante
        self.tipo_obra= tipo_obra
    def obra(self):
        print(f"El tipo de categoria del libro es {self.tipo_obra}")
    def estante(self):
        print(f"El numero de estante que quedo almacenado fue el #{self.num_estante}")

        



