#La función enumerate( ) nos facilita llevar la cuenta de las iteraciones, a través de un contador de índices de un iterable, que se puede utilizar de manera directa en un loop, o convertirse en una lista de tuplas con el método list( ).
#Facilita acceder a los indices de un objeto
print("Recorrer lista y ver sus indices sin utilizar enumerated()")
lista = ['a','b','c']
indice =0
for item in lista:
    print(indice,item)
    indice+=1
print()

#####################
print("Recorrer lista y ver sus indices utilizando enumerated(), retorna una tupla con el indice y el valor")
lista = ['a','b','c']
for item in enumerate(lista):
    print(item)
print()

#####################
print("Recorrer lista y ver sus indices utilizando enumerated(), retorna una tupla y son recopilados utilizando asignacion multiple")
lista = ['a','b','c']
for indice, item in enumerate(lista):
    print(f"{indice} {item}")
print()


#####################
print("Recorrer un range y ver sus indices utilizando enumerated(), retorna una tupla y son recopilados utilizando asignacion multiple")
for indice, item in enumerate(range(50,55)):
    print(f"{indice} {item}")
print()

####################3
#Convertir una lista en una lista de tupla con enumerated() que contenga el indice y valor
print("Convertir una lista en una tupla con enumerated()")
lista = ['a','b','c']
mi_tupla= list(enumerate(lista))
print(mi_tupla)

print("\nEncontrar el valor del primer elemento en la tupla mi_tupla[1][1]")
print(mi_tupla[1][1])
print()

#################################
print("Ejemplo recorrer lista de string\n")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
tupla=list(enumerate(lista_nombres))
for indice, nombre in tupla:
    print(f'{nombre} se encuentra en el índice {indice}')


#################
#Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".
#Llama a la lista obtenida con el nombre de variable lista_indices .
print("Ejemplo recorrer un string y convertir en una tupla\n")
nombre="Python"
lista_indices = list(enumerate(nombre))
for indice, nombre in lista_indices:
    print(f'{nombre} se encuentra en el índice {indice}')
print()

######################
#Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:
print("Imprime en pantalla únicamente los índices de aquellos nombres de una lista a continuación, que empiecen con M:\n")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
tupla=list(enumerate(lista_nombres))
for indice, nombre in tupla:
    if nombre[0] == 'M':
        print(f"{indice} -  {nombre}")
