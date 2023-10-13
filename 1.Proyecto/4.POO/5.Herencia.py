'''
La herencia es el proceso mediante el cual una clase puede tomar métodos y atributos de una clase superior, evitando
repetición del código cuando varias clases tienen atributos o métodos en común.

Es posible crear una clase "hija" con tan solo pasar como parámetro la clase de la que queremos heredar:
Una clase hija puede sobrescribir los métodos de una clase padre, o incluso crear unos nuevos

Para indicar una herencia, basta con pasarle como argumento a una clase, el nombre de la clase a heredar => class Animal(Nombre_Clase_Heredar):
'''

print("Ejemplo de herencia entre una clase Personaje y la clase Mago, en este caso Mago hereda de Personaje.\n")
class Personaje:
    def __init__(self, nombre, arma):
        self.nombre = nombre
        self.arma = arma

#La clase Mago en este caso hereda de la clase Personaje
class Mago(Personaje):
    pass

hechicero = Mago("Merlín", "caldero")
print(f"El hechichero {hechicero.nombre} tiene como arma un {hechicero.arma}.\n")

############################################################################################
print("Ejemplo herencia\n")
class Animal:
    def __init__(self, edad, color):
        self.edad=edad
        self.color=color
    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

class Perro(Animal):
    pass

print("Verificar tipo de la clase Pajaro, para comprobar herencia de la clase animal mediante 'Pajaro.__bases__'.")
print(Pajaro.__bases__)

print("\nVerificar las subclases que heredan de la clase Animal mediante 'Animal.__subclasses__()'.")
print(Animal.__subclasses__())

print("\nVerificar heredacion de métodos de la clase animal en la clase Pajaro: ")
piolin=Pajaro(2,'amarillo')
piolin.nacer()
print(f"El pajaro instanciado es de color: {piolin.color}")