#Random permite generar numeros aleatorios
#Se debe importar la libreria en python de Random
#importar libreria
from random import *  #Si se necesita muchos metodos de una libreria
#from random import randint; # Si de random solo necesitamos el metodo randint()

print("Generar numero entero aleatorio con randint()")
aleatorio=randint(1,50)
print(aleatorio)
print()

print("Generar numero flotante aleatorio con uniform()")
aleatorio=uniform(1,5)
print(aleatorio)
print()

print("Generar numero flotante aleatorio con uniform() y redondearlo con metodo round() a 2 decimales")
aleatorio=round(uniform(1,5),2)
print(aleatorio)
print()

print("Generar numero aleatorio entre 0 y 1 con random, el cual es un metodo que genera una fraccion de un entero")
aleatorio=random()
print(aleatorio)
print()


print("Escoge una elemento aleatorio dentro de una lista")
colores =['azul','rojo','verde','amarillo']
aleatorio=choice(colores)
print(aleatorio)
print()

print("Escoge una elemento aleatorio dentro de una lista")
colores =[False, 1,2,True, 3,4,5,'rojo','verde','amarillo']
aleatorio=choice(colores)
print(aleatorio)
print()


print("Mezclar en una lista los elementos y ordenarlos de forma distinta, por ejemplo un juego de naipes")
numeros=list(range(5,50,5))
print("Lista original")
print(numeros)
aleatorio=shuffle(numeros)
print("Lista mezclada")
print(numeros)
print()