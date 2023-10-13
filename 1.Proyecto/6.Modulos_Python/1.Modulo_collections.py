'''
El módulo Collections amplía los tipos de contenedores disponibles en Python. Un contenedor almacena diferentes
objetos y proporciona una nueva forma de acceder e iterar sobre los mismos.
'''
from collections import Counter, defaultdict, namedtuple, deque

numeros = [8,4,5,3,43,5,6,3,5,67,7,8,9,1,32,3,45,5,6,7,8,8,8,45,34,4]
print("Método counter nos retorna un diccionario con el número de veces que se repite cada elemento en un objeto")
print("Su estructura es: {elemento_lista: número_repeticiones_elemento}\n")
print(Counter(numeros))
print()

texto="Hola, bienvenido a este espacio de sabiduria en Python"
print("Método counter sirve para contar elementos de un string")
print(Counter(texto))
print()


texto="al pan pan y al vino vino"
print("También podemos contar las palabras que se repiten en una frase, en este caso utilizamos split() para convertir la frase en una lista separada por espacios.")
print(Counter(texto.split()))
print()

print("Método most_common() retorna en tupla los elementos más frecuentes de mayor a menor, puedo indicar como parametro cuantos elementos frecuentes quiero observar")
lista_numeros=[1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,4]
serie=Counter(lista_numeros)
print(serie.most_common())
print("Observar el primero elemeto más frecuente serie.most_common(1))")
print(serie.most_common(1))
print("Observar los dos elemetos más frecuente serie.most_common(1)) y asi sucesivamente")
print(serie.most_common(2))

print("\nCrear una lista nueva con los elementos más frecuentes sin elementos duplicados => list(serie)")
print(list(serie))
print()

print("*"*50)
print("*"*50)
print("*"*50+"\n")
print("Método defaultdict del módulo Collections:")

mi_dic={'uno':'verde','dos':'azul','tres':'rojo'}
print(mi_dic['tres'])
#print(mi_dic['cuatro']) #Presenta error si no esta en el diccionario
print("Utilizar defaultdict, el cual permite crear un diccionario y verificar los casos en el cual no exista un elemento, coloca para la clave que se verifica el valor por defector 'nada'\n")
mi_dic=defaultdict(lambda : 'nada')
mi_dic['uno']='verde'
print(mi_dic['uno'])
print(mi_dic['cuatro'])
print(mi_dic)  #Impresion del diccionario creado
print()

print("*"*50)
print("*"*50)
print("*"*50+"\n")
print("Método namedtuple del módulo Collections:")
mi_tupla=(500,18,65)
print("Para acceder a un valor de la tupla lo hacemos por medio de su indice => mi_tupla[1]")
print(mi_tupla[1])

print("\nNo obstante, namedtuple permite acceder a los valores de una tupla por medio de su valor. Podemos crear objetos a partir de este método, ejemplo:  ")
Persona=namedtuple('Persona',['nombre','altura','peso'])
jhonnyer=Persona('Jhonnyer',1.63,79)
print(jhonnyer.altura)
print(jhonnyer.peso)
print("\nTambién podemos acceder a un valor de la tupla por medio de su indice")
print(jhonnyer[2])
print()


'''Una doble cola o deque (double-ended queue) se puede implementar en Python utilizando el módulo collections. El módulo collections proporciona una clase llamada deque que es perfecta para este propósito, ya que permite la inserción y eliminación eficiente de elementos tanto por el lado izquierdo como por el lado derecho de la cola.
Primero, debes importar la clase deque del módulo collections. Luego, puedes crear una instancia de deque y agregar los elementos iniciales proporcionados. Aquí tienes un ejemplo de cómo hacerlo:'''
print("*"*50)
print("*"*50)
print("*"*50+"\n")
print("\nEjemplo manejo de doble cola o deque la cual permite insertar o eliminar elementos de una colección por ambos extremos:\n")
# Crear una deque e inicializarla con los elementos iniciales
lista_ciudades = deque(["Londres", "Berlín", "París", "Madrid", "Roma", "Moscú"])

# Agregar elementos por la izquierda
lista_ciudades.appendleft("Nueva York")
lista_ciudades.appendleft("Tokio")

# Agregar elementos por la derecha
lista_ciudades.append("Pekín")
lista_ciudades.append("Sidney")
print(lista_ciudades)

#Remover elementos  por izquierda
lista_ciudades.popleft()
#Remover elementos  por derecha
lista_ciudades.pop()

# Imprimir la deque resultante
print(lista_ciudades)
