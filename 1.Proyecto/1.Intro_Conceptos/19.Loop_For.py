#Loop es un bucle que hace que un bloque de codigo se repita mas de una vez
#optimiza el codigo
#Hace que un bloque de codigo se ejecute multiples veces hasta que se cumpla una condicion
#En programacion existen objetos iterables que se peuden recorrer como por ejemplo una lista, se repite el codigo por cada elemento de la lista

#A diferencia de otros lenguajes de programación, los loops for en Python tienen la capacidad de iterar a lo largo de los elementos de cualquier secuencia (listas, strings, entre otros), en el orden en que dichos elementos aparecen.
#Loops/bucles: son secuencias de instrucciones de código que se ejecutan repetidas veces
# Iterables: son objetos en Python que se pueden recorrer (o iterar) a lo largo de sus elementos

#Iteracion lista, elemento es una variable temporal donde almacena la informacion de cada elemento de la lista
print("Iteracion lista");
nombres=['Juan', 'Ana', 'Carlos','Belen','Fran']
for elemento in nombres:
    print("Hola "+elemento)
print()

#Iteracion lista, elemento es una variable temporal donde almacena la informacion de cada elemento de la lista
#Index permite obtener la posicion de cada elemento dentro de la lista
print("Iteracion lista y posicion de elementos");
nombres=['Juan', 'Ana', 'Carlos','Belen','Fran']
for elemento in nombres:
    posicion_real=nombres.index(elemento);
    posicion=posicion_real+1
    print(f"Hola {elemento}, estas en la posición: {posicion}. Dentro de la lista tu posiscion real es: {posicion_real}")
print()

#Iteracion lista, verificar si un nombre empieza con una letra cualquiera mediante el metodo startswith()
print("Iteracion lista y condicional utilizando metodo startswith()\n");
nombres=['Juan', 'Ana', 'Carlos','Belen','Fran']
for elemento in nombres:
    if elemento.startswith('A'):
        print(f"Hola {elemento}, estas en la posición: {posicion}. Dentro de la lista tu posiscion real es: {posicion_real}")
    else:
        print("Nombre que no comienza con A es "+elemento)
print()

#Iteracion lista de enteros
print("Ejemplo suma de valores dentro de una lista por medio de una iteracion")
numeros=[1,2,3,4,5]
suma=0
for num in numeros:
    suma=suma+num
    print(f"Resultado parcial de la suma es: {suma}")
print(f"\nResultado final de la suma es: {suma}")


#Iteracion lista de enteros
print("Ejemplo iteracion de un texto")
texto="Python es genial"
for elemento in texto:
    print(elemento)
print()

#Iteracion de una tupla
print("Iteracion de una tupla")
tupla = (2,'fin',True)
for elemento in tupla:
    print(elemento)
print()

#Iteracion de una lista formada por otras listas
print("Iteracion de una lista formada por otras listas")
lista= [[1,2],[3,4],[5,6]]
for elemento in lista:
    print(elemento)
print()

#Iteracion de una lista formada por otras listas
print("Iteracion de una lista formada por otras listas accediendo a su objetos dentro de la lista por medio de asignacion de multiples variables")
lista= [[1,2],[3,4],[5,6]]
for elem1, elem2 in lista:
    print(f"{elem1} *** {elem2}")
print()

#Iteracion de una lista formada por otras listas
print("Iteracion de una lista formada por otras listas accediendo a su objetos dentro de la lista por medio de asignacion de multiples variables y sumandolos")
lista= [[1,2],[3,4],[5,6]]
for elem1, elem2 in lista:
    print(f"La suma de {elem1} + {elem2} es igual a {elem1+elem2}")
print()


#Iteracion dentro de un diccionario
print("Iteracion dentro de un diccionario, obteniendo las claves")
diccionario={'clave1':'a','clave2':'b','clave3':'c'}
for item in diccionario:
    print(f"{item}")
print()


#Iteracion dentro de un diccionario
print("Iteracion dentro de un diccionario, obteniendo las claves por medio del metodo keys()")
diccionario={'clave1':'a','clave2':'b','clave3':'c'}
for item in diccionario.keys():
    print(item)
print()

#Iteracion dentro de un diccionario
print("Iteracion dentro de un diccionario, obteniendo los valores por medio del metodo values()")
diccionario={'clave1':'a','clave2':'b','clave3':'c'}
for item in diccionario.values():
    print(item)
print()

#Iteracion dentro de un diccionario
print("Iteracion dentro de un diccionario, obteniendo las claves y valores por medio del metodo items(), retornando la clave y  el valor en una tupla")
diccionario={'clave1':'a','clave2':'b','clave3':'c'}
for item in diccionario.items():
    print(f"{item} es de tipo: {type(item)}")
print()

#Iteracion dentro de un diccionario
print("Iteracion dentro de un diccionario, obteniendo las claves y valores por medio del metodo items() y la asignacion de multiples variables")
diccionario={'clave1':'a','clave2':'b','clave3':'c'}
for clave, valor in diccionario.items():
    print(f"Clave: {clave} - Valor: {valor}")
print()

#Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente
print("Suma de numeros pares e impares separadamente")
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
list_impar=[]
list_par=[]

for el in lista_numeros:
    if el % 2  != 0:
        suma_impares=suma_impares+el
        list_impar.append(el)
    else:
        suma_pares=suma_pares+el
        list_par.append(el)

print("Listado de pares y suma total")
print(list_par)
print(suma_pares)
print("Listado de impares y suma total")
print(list_impar)
print(suma_impares)
print()
