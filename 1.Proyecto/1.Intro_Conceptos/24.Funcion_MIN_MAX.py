#La función min( ) retorna el item con el valor más bajo dentro de un iterable. La función max( ) funciona del mismo modo, devolviendo el valor más alto del iterable. Si el iterable contiene strings, la comparación se realiza alfabéticamente.
#MIN permite detectar los valores mas bajos dentro de una colección, funciona con valores numericos o alfabeticos
#MAX permite detectar los valores mas altos dentro de una colección, funciona con valores numericos o alfabeticos
print("Funcion MIN con enteros")
menor=min(59, 23, 54, 76, 3)
print(menor)
print()

print("Funcion MAX con enteros")
mayor=max(59, 23, 54, 76, 3)
print(mayor)
print()

print("Funcion MAX y MIN con una lista de enteros")
lista = [59, 23, 54, 76, 3]
mayor=max(lista)
print(mayor)
print(f"El número menor es {min(lista)}")
print()

###Funcion min y max con lista de string que se ordenan alfabeticamente
print("MIN Y MAX en una lista de string\n")
texto=['juan','pablo','andrea']
print(f"El nombre alfabeticamente mayor es: {max(texto)}")
print(f"El nombre alfabeticamente menor es: {min(texto)}\n")


print("MIN Y MAX en una cadena de caracteres\n")
nombre='Hola mundo' #Cada caracter ocupa una posicion, el caracter menor en este caso es el espacio vacio
print(f"El nombre alfabeticamente mayor es: '{max(nombre)}'")
print(f"El nombre alfabeticamente menor es: '{min(nombre)}'\n")


print("MIN Y MAX en un diccionario, en este caso evalua el valor pero retorna la clave que contiene el valor mas alto o mas bajo\n")
diccionario={'c1':45,'c2':12,'c3':14}
print(f"El valor mayor en el diccionario es: '{max(diccionario)}'")
print(f"El valor menor en el diccionario es: '{min(diccionario)}'\n")

print("MIN Y MAX en un diccionario, en este caso evalua el valor y lo retorna utilizando el metodo values()\n")
diccionario={'c1':45,'c2':12,'c3':14}
print(f"El valor mayor en el diccionario es: '{max(diccionario.values())}'")
print(f"El valor menor en el diccionario es: '{min(diccionario.values())}'\n")

#Ejemplo valor maximo
print("Ejemplo valor maximo numeros enteros,flotantes y resultados aritmeticos")
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)
print()

######
#Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:
print("Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango")
maximo=max(lista_numeros)
minimo=min(lista_numeros)
rango=maximo-minimo
print(rango)
print()

###
print("""Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario y almacena dicho valor en una variable llamada edad_minima.
También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.""")
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima=min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print()
print(f"Edad minima {edad_minima}")
print(f"Ultimo nombre {ultimo_nombre}")