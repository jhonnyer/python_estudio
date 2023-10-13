#Comprension de listas
palabra = 'python'
lista=[]
print("Crear lista de un string normal")
for letra in palabra:
    lista.append(letra)
print(lista)
print()

##########################################################
#La palabra letra dentro de la lista debe ser igual dentro de corchetes [letra for letra in palabra]
print("Crear lista de un string por medio de la comprension de lista => lista=[letra for letra in palabra]")
print("En este caso, cada elemento dentro de la lista va a ser una letra de cada letra dentro de palabra")
palabra = 'animal'
lista=[letra for letra in palabra]
print(lista)
print()


##########################################################
#Comprension de lista númerica
print("Comprension de lista númerica => lista=[n for n in range(0,21,2)]")
lista=[n for n in range(0,21,2)]
print(lista)
print()

##########################################################
#Comprension de lista númerica utilizando operacion aritmetica, en este caso cada elemento dentro del rango se divide por 2 y se guarda en la lista
print("Comprension de lista númerica utilizando operación aritmética => lista=[n/2 for n in range(0,21,2)]")
lista=[n/2 for n in range(0,21,2)]
print(lista)
print()


##########################################################
#Comprension de lista númerica utilizando operacion aritmetica y un condicional if para verificar que datos añadir a la lista, en este caso que el número multiplicado por 2 sea mayor que 10
print("Comprension de lista númerica utilizando operacion aritmetica y un condicional if para verificar que datos añadir a la lista => lista=[n for n in range(0,21,2) if n * 2 >10]")
lista=[n for n in range(0,21,2) if n * 2 >10]
print(lista)
print()


##########################################################
#Comprension de lista númerica utilizando operacion aritmetica y un condicional if para verificar que datos añadir a la lista, en este caso que el número multiplicado por 2 sea mayor que 10. Sino se cumple, se tiene la condicion else y se añade la palabra no
#NOTA: En este caso if else se añade la condicion antes del for
print("Comprension de lista númerica utilizando operacion aritmetica y un condicional if para verificar que datos añadir a la lista. También se utiliza condicion else. para agregar 'no' a la lista si no cumple la condición")
print("NOTA: En este caso if else se añade la condicion antes del for  =>  lista=[n if n*2 >10 else 'no' for n in range(0,21,2)]")
lista=[n if n*2 >10 else 'no' for n in range(0,21,2)]
print(lista)
print()

##########################################################
#Comprension de lista númerica utilizando operacion aritmetica y un operador and
#NOTA: En este caso if,  else se añade la condicion antes del for y un operador and para la condicion
print("Comprension de lista númerica utilizando operacion aritmetica y un condicional if para verificar que datos añadir a la lista. También se utiliza condicion else. para agregar 'no' a la lista si no cumple la condición")
print("NOTA: En este caso if,  else se añade la condicion antes del for y un operador and para la condicion  => lista=[n if n*2 >=10 and n== 6 else 'no' for n in range(0,21,2)]")
lista=[n if n*2 >=10 and n== 6 else 'no' for n in range(0,21,2)]
print(lista)
print()


##########################################################
#Comprension de lista númerica utilizando operacion aritmetica y un operador or
#NOTA: En este caso if,  else se añade la condicion antes del for y un operador or para la condicion
print("Comprension de lista númerica utilizando operacion aritmetica y un condicional if para verificar que datos añadir a la lista. También se utiliza condicion else. para agregar 'no' a la lista si no cumple la condición")
print("NOTA: En este caso if,  else se añade la condicion antes del for y un operador or para la condicion  => lista=[n if n*2 >10 or n*3== 6 else 'no' for n in range(0,21,2)]")
lista=[n if n*2 >10 or n*3== 6 else 'no' for n in range(0,21,2)]
print(lista)
print()

#####################################################
print("\nA partir de una lista en pie, crear una lista en metros")
pies=[10,20,30,40,50]
metros=[p*3.281 for p in pies]
print(metros)

########
print("\nA partir de una lista numerica crear una nueva lista con valores pares")
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [v for v in valores if v%2 ==0]
print(valores_pares)

############
print("\nConvertir lista grados Fahrenheit a grados celsius")
temperatura_fahrenheit = [32, 212, 275]
grados_celsius=[(n-32)*(5/9) for n in temperatura_fahrenheit]
print(grados_celsius)