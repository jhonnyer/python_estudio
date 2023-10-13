'''
La cohesión se refiere al grado de relación entre los elementos de un módulo. Cuando diseñamos una función, debemos identificar de un modo bien específico qué tarea va a realizar, reduciendo su finalidad a un objetivo único y bien definido.

En resumen: para que una función sea cohesiva debe hacer solo una cosa, y si tiene que hacer más de una cosa, estas deben tener una alta relación entre sí. Cuantas más cosas haga una función sin relación entre sí, más complicado será entender el código.

Existen dos tipos de cohesión:

Cohesión débil: indica que la relación entre los elementos es baja, y por lo tanto no tienen una única funcionalidad.
Cohesión fuerte: indica que existe una alta relación entre los elementos existentes dentro del módulo. Este debe ser nuestro objetivo al diseñar programas.
'''

print("Ejemplo cohesión fuerte: \n")

def suma(num1, num2):
    resultado =num1 + num2
    return resultado

print(suma(4,5))

print("\nEjemplo 2 cohesión fuerte: ")

def suma(lista_numeros):
    resultado = 0
    for n in lista_numeros:
        resultado += n
    return resultado

lista= [6,4,2,4]
print(suma(lista))
print()

print("\nEjemplo cohesión debil, en este caso en la misma función se píde que ingrese los números. El problema radica, si el usuario ya tiene los números: \n")

def sumatoria():
    num1 = float(input("Elige un número: "))
    num2 = float(input("Elige otro número: "))
    resultado = num1 + num2
    return resultado

print(sumatoria())