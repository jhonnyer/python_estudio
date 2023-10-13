'''
El polimorfismo es el pilar de la POO mediante el cual un mismo método puede comportarse de diferentes maneras según el
objeto sobre el cual esté actuando, en función de cómo dicho método ha sido creado para la clase en particular.

Objetos de diferentes clases pueden tener el mismo nombre del método, pero aplicado a otra funcionalidad según el objeto.

El método len( ) funciona en distintos tipos de objetos: listas, tuplas, strings, entre otros. Esto se debe a que para Python,
lo importante no son los tipos de objetos, sino lo que pueden hacer: sus métodos.
'''

print("Ejemplo 1 de Polimorfismo, clase Perro y Gato: ")

class Perro:
    def hablar(self):
        print("Guau!")
class Gato:
    def hablar(self):
        print("Miau!")

hachiko = Perro()
garfield = Gato()
for animal in [hachiko, garfield]:
    animal.hablar()

#################################################################################
print("\nEjemplo 2 de Polimorfismo, clase Vaca y Oveja: ")

class Vaca:
    def __init__(self, nombre):
        self.nombre=nombre
    def hablar(self):
        print("Mi vaca "+self.nombre+" dice muuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Mi oveja "+self.nombre + " dice bee")

mi_vaca = Vaca('Aurora')
mi_oveja = Oveja('Nube')

print("\nCrear una lista de animales y recorrerlo con un for que llame el método hablar() de cada clase:")
for animal in [mi_vaca, mi_oveja]:
    animal.hablar()

print("\nCrear una lista distinto de animales y recorrerlo con un for que llame el método hablar() de cada clase:")
mi_vaca1 = Vaca('Aurora')
mi_vaca2 = Vaca('Lulu')
mi_oveja = Oveja('Nube')
lista=[mi_oveja, mi_vaca1, mi_vaca2]
for animal in lista:
    animal.hablar()

print("\nEl código anterior, optimizarlo mediante una función que llame el método hablar() de cada clase, independiente el tipo de instancia que se le pase al método: ")
def animal_habla(animal):
    animal.hablar()

animal_habla(mi_vaca2)
animal_habla(mi_vaca1)
animal_habla(mi_oveja)
print()


######################################
#La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.
print("La función len() en Python tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.")
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for objeto in [palabra, lista, tupla]:
    print(len(objeto))
