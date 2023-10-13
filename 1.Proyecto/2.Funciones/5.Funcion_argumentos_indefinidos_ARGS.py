#args:  En aquellos casos en los que no se conoce de antemano el número exacto de argumentos que se deben pasar a una
#función, se debe utilizar la sintaxis *args para referirse a todos los argumentos adicionales luego de los obligatorios.
#*args se define como argumentos variables
#*args es una convención, sin embargo lo importante es el simbolo * y puede ir cualquier palabra despues (*aviones), pero es recomendable utilizar *args
#El nombre *args no es mandatorio pero si es sugerido como buena práctica.
#Cualquier nombre iniciado en * referirá a estos argumentos de cantidad variable.
#La función recibirá los argumentos indefinidos *args en forma de tupla, a los que se podrá acceder o iterar de las formas habituales dentro del bloque de código de la función.
# => def mi_funcion(arg_1, arg_2, *args):
# => mi_funcion("ejemplo", 25, 40, 75, 10), en este caso (40,75,10) se reciben como tuplas y son lor args adicionales no obligatorios

print("Ejemplo verificar si existe un argumento adicional con *args, y procesarlo")
def procesar_numero(a,b, *args):
    resultado=0
    if len(args) == 0:
        # Si no se pasan argumentos adicionales, solo sumar
        resultado=a+b
    elif len(args) == 1 and isinstance(args[0], int):
        # Si se pasa un argumento adicional y es un entero, dividir el resultado de la suma
        resultado=(a+b)/args[0]
    else:
        raise ValueError("La función acepta solo dos enteros o tres argumentos enteros (para dividir).")
    return resultado


# Ejemplos de uso
resultado1 = procesar_numero(2, 3)
print("Resultado 1:", resultado1)  # Suma: 2 + 3 = 5
resultado2 = procesar_numero(2, 3, 2)
print("Resultado 2:", resultado2)  # División: (2 + 3) / 2 = 2.5
print()

############################################
print("Ejemplo sumar los argumentos que se envian en una funcion que sabemos que son una tupla")
def suma(*args):
    total=0
    for arg in args:
        total+=arg
    return total

print(suma(5,7,2,3))


############################################
print("Ejemplo sumar los argumentos que se envian en una funcion que sabemos que son una tupla mediante metodo sum()")
def suma(*args):
    return sum(args)
print(suma(5,7,2,3))
print()

print("Ejemplo suma potencia al cuadrado de elementos ingresados en la funcion")
def suma_cuadrados(*args):
    total=0
    for ar in args:
        total=total+ar**2
    return total

print(suma_cuadrados(5,7,2,3))
print()

print("Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).")
def suma_absolutos(*args):
    # Utilizamos una comprensión de lista para calcular los valores absolutos y los sumamos
    suma = sum(abs(valor) for valor in args)
    return suma

# Ejemplos de uso
resultado1 = suma_absolutos(1, -2, 3, -4, 5)
print("Resultado 1:", resultado1)  # Resultado: 15 (|1| + |2| + |3| + |4| + |5|)

resultado2 = suma_absolutos(-10, -20, -30, -40, -50)
print("Resultado 2:", resultado2)  # Resultado: 150 (|10| + |20| + |30| + |40| + |50|)
print()

#######################################
print("Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números. La función debe devolver el siguiente mensaje: {nombre}, la suma de tus números es {suma_numeros}")
def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje

# Ejemplo de uso:
nombre = "Juan"
resultado = numeros_persona(nombre, 1, 2, 3, 4, 5)
print(resultado)  # Salida: "Juan, la suma de tus números es 15"
