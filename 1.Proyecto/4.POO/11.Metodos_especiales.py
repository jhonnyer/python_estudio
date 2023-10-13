#Métodos especiales
'''
Puedes encontrarlos con el nombre de métodos mágicos o dunder methods (del inglés: dunder = double underscore, o doble guión
bajo). Pueden ayudarnos a sobrescribir métodos incorporados de Python sobre nuestras clases para controlar el resultado devuelto.

Son escritos con doble guión bajo  __Nombre_Metodo_Especial__

'''

print("Ejemplo Métodos Especiales existentes, en este caso el método len:")
lista=[1,1,1,1,1,1]
print(len(lista))

print("\nEjemplo sobreescribir el método str y len como un método especial de una clase, en este caso modificar el comportamiento del método especial str() y len()")
class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print(f"Se ha eliminado el cd con titulo: {self.titulo}")



mi_cd=CD('Pink Floy','The Wall', 24)
print(str(mi_cd))
print(len(mi_cd))
print()

print("Funcion especial 'del' que permite eliminar instancias de una clase")
del mi_cd
#print(mi_cd)  #NO VA A FUNCIONAR porque ya no existe el objeto

print("\nEjemplo Métodos Especiales Sobreescritos:")
class Libro:
    def __init__(self, autor, titulo, cant_paginas):
        self.autor = autor
        self.titulo = titulo
        self.cant_paginas = cant_paginas

    def __str__(self):
        return f'Título: "{self.titulo}" , escrito por {self.autor}'

    def __len__(self):
        return self.cant_paginas

libro1 = Libro("Stephen King",  "It", 1032)
print(str(libro1))
print(len(libro1))
print()


print("Ejemplo libros. ")


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return int(self.cantidad_paginas)

    def __del__(self):
        print("Libro eliminado")

mi_libro=Libro('Cien años de soledad','Gabriel Garcia Márquez',1590)
print(str(mi_libro))
print(len(mi_libro))
del  mi_libro
