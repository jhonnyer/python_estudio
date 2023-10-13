#Interación entre funciones
#Las salidas de una determinada función pueden convertirse en entradas de otras funciones. De esa manera, cada función realiza una tarea definida, y el programa se construye a partir de la interacción entre funciones
from random import *

print("Ejemplo juego escoger el palito indicado")
palitos=['-','--','---','----']

#Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#Pedir un intento
def probar_suerte():
    intento=''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

#Comprobar intento
def chequear_intento(lista, intento):
    if lista[intento-1] == '-':
        print("Lavar los platos")
    else:
        print("Te has salvado")
    print(f"Tu selección al azar es: '{lista[intento-1]}'")

palitos_mezclados=mezclar(palitos)
seleccion=probar_suerte()
chequear_intento(palitos_mezclados,seleccion)
print()

print("Ejemplo  juego de dados, función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:")
'''def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2
'''
#Funcion lanzar dados mejorada mediante una lista y retornando una tupla
#el uso del guion bajo _ en lugar de una variable regular indica que no estamos interesados en los valores individuales generados por el bucle.
#En otras palabras, estamos generando dos números aleatorios entre 1 y 6 usando random.randint(1, 6), pero no necesitamos los valores en sí, solo queremos generarlos dos veces. Usar _ es una convención común para indicar que la variable no se usará posteriormente en el bucle. Es un indicador para otros programadores de que la variable se ignora intencionalmente.
def lanzar_dados():
    resultados = [randint(1, 6) for _ in range(2)]
    return tuple(resultados)

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2

    if suma_dados <= 6:
        mensaje = f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        mensaje = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        mensaje = f"La suma de tus dados es {suma_dados}. ¡Felicidades!"

    return mensaje


# Lanzamos los dados
dado1, dado2  = lanzar_dados()
# Evaluamos la jugada
mensaje_resultado = evaluar_jugada(dado1, dado2)

# Imprimimos el mensaje
print(mensaje_resultado)
print()

#####################################
print("Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse")
def reducir_lista(lista):
    # Elimina duplicados y ordena la lista
    lista_sin_duplicados = list(set(lista))
    # Si la lista no está vacía, elimina el valor más alto
    if lista_sin_duplicados:
        lista_sin_duplicados.remove(max(lista_sin_duplicados))
    return lista_sin_duplicados

def promedio(lista):
    if not lista:
        return None  # Manejar lista vacía
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

# Ejemplo de uso:
lista_numeros = [1, 2, 15, 7, 2]
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)
print("Lista inicial:", lista_numeros)
print("Lista reducida:", lista_reducida)
print("Promedio de la lista reducida a dos decimales:", round(resultado_promedio,2))
print()


###############################################
print("Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados 'Cara' o 'Cruz', y no debe recibir argumentos para funcionar. Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).")

def lanzar_moneda():
    resultado = choice(["Cara", "Cruz"])
    return resultado

def probar_suerte(resultado_moneda, lista_numeros):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif resultado_moneda == "Cruz":
        print("La lista fue salvada")
        return lista_numeros

# Lista de números de ejemplo
lista_numeros = [1, 2, 3, 4, 5]

# Lanzar la moneda
resultado_moneda = lanzar_moneda()

# Probar suerte con la lista
nueva_lista = probar_suerte(resultado_moneda, lista_numeros)
print("Nueva lista:", nueva_lista)
