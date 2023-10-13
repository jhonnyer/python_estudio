#POO => Programación orientada a objetos
#Clases nos permite definir objetos, tiene atributos (carecteristicas) y métodos (Funciones que puede realizar un objeto)

'''
Python es un lenguaje de Programación Orientado a Objetos (POO). Como tal, utiliza y manipula objetos, a través de sus métodos y
propiedades. Las clases son las herramientas que nos permiten crear objetos, que "empaquetan" datos y funcionalidad juntos.

Podemos pensar a las clases como el "plano" o "plantilla" a partir del cual podemos crear objetos individuales, con propiedades y métodos asociados:

Pasos:

1. Crear la clase => class Objeto:
2. Creación objeto a partir de la clase => nuevo_objeto = Objeto()
    * Los objetos creados son instancias de una clase
'''
print("Creacion de clases y una instancia (objeto) de esta clase.\n")
class Pajaro:
    pass

#Creacion de una instancia (objeto) de la clase Pajaro.
mi_pajaro = Pajaro()
print(mi_pajaro)
print(type(mi_pajaro))
print()

#Cada instancia creada de la clase Pajaro ocupa una unidad fisica de memoria distinta
otro_pajaro = Pajaro()
print(mi_pajaro)
print(type(mi_pajaro))