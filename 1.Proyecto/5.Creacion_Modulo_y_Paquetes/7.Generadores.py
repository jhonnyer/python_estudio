'''
Los generadores son tipos especiales de funciones que devuelven un iterador que no almacena su contenido
completo en memoria, sino que "demora" la ejecución de una expresión hasta que su valor se solicita.


Dado que un ordenador no cuenta con memoria infinita, no podría generarse una secuencia de
números sin límite sin la ayuda de un generador. Lo mismo ocurre con datos que, sin ser infinitos,
ocuparían demasiado espacio en memoria de almacenarse repentinamente.

Mejorar el rendimiento en termino de espacio en un ordenaror.
'''
print("\nEjemplo 1 función generadora: ")
def secuencia_infinita():
    num = 0
    while True:
        yield num
        num += 1

generador = secuencia_infinita()
print(next(generador))
print(next(generador))
print(next(generador))

###################################################
print("\nEjemplo 2 función generadora: ")

def mi_funcion():
    return 4

def mi_generador():
    yield 4

print(mi_funcion())
print(mi_generador())  #Imprime que hay un objeto en el generador pero no lo ha producido

generador=mi_generador()
print("\nCon next podemos pedir el dato que tiene el generador y continuar al otro valor")
print(next(generador))
print()


###################################################
print("\nEjemplo 3 función generadora en una lista de números a partir de un generador: ")

def mi_funcion():
    lista=[]
    for x in range(1,5):
        lista.append(x*10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x*10

print(mi_funcion())
print(mi_generador())  #Imprime que hay un objeto en el generador pero no lo ha producido

generador=mi_generador()
print("\nCon next podemos pedir el dato que tiene el generador y continuar al otro valor")
print(next(generador))
print(next(generador))
print("Los datos que no se han generado aún no existe y no ocupa espacio de memoria")
print(next(generador))
print(next(generador))
#print(next(generador)) #Cuando ya no existen más datos generados, aparece un mensaje de error.
print()

##########################################################
print("\nFunción generadora que retorna varios datos generados: ")
def mi_generadored():
    x=1
    yield x

    x+=1
    yield x

    x+=1
    yield x

g=mi_generadored()
print(next(g))
print(next(g))
print(next(g))
print("Generador no detiene o interrumpe la funcion, sino que se ejecuta apartir de lo que se esta ejecutando.")
print("En este caso, cada que se llame la funcion next(g), se sigue a un paso siguiente (yield) de la función generadora\n")
print()


################################
print('''Generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.''')
def generador_infinito():
    num = 1
    while True:
        yield num
        num += 1

# Crear el generador
generador = generador_infinito()

# Ejemplos de uso:
print(next(generador))  # Devuelve 1
print(next(generador))  # Devuelve 2
print(next(generador))  # Devuelve 3
print()
# Y así sucesivamente, seguirá devolviendo números consecutivos infinitamente


#######################
print('''Generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).''')
def generador_multiplos_de_7():
    num = 7
    while True:
        yield num
        num += 7

# Crear el generador
generador = generador_multiplos_de_7()

# Ejemplos de uso:
print(next(generador))  # Devuelve 7
print(next(generador))  # Devuelve 14
print(next(generador))  # Devuelve 21
print()

##############################

print('''Generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:

"Te quedan 3 vidas"

"Te quedan 2 vidas"

"Te queda 1 vida"

"Game Over"

Almacena el generador en la variable perder_vida\n''')

def generador_perder_vida(vidas_iniciales):
    vidas = vidas_iniciales
    while vidas > 0:
        if vidas == 1:
            yield "Te queda 1 vida"
        else:
            yield f"Te quedan {vidas} vidas"
        vidas -= 1
    yield "Game Over"

# Crear el generador con 3 vidas iniciales
perder_vida = generador_perder_vida(3)

# Ejemplos de uso:
print(next(perder_vida))  # Devuelve "Te quedan 3 vidas"
print(next(perder_vida))  # Devuelve "Te quedan 2 vidas"
print(next(perder_vida))  # Devuelve "Te queda 1 vida"
print(next(perder_vida))  # Devuelve "Game Over"
# Si se llama a next después de "Game Over", seguirá devolviendo "Game Over"


#####
print("\nSoluciones opcionales: ")

print("Secuencia infinita: ")
def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num

generador = secuencia_infinita()
print(next(generador))
print(next(generador))
print(next(generador))


############################
print("\nSecuencia multiplos de 7: ")
def multiplos_siete():
    num = 1
    while True:
        yield 7 * num
        num += 1


generador = multiplos_siete()
print(next(generador))
print(next(generador))
print(next(generador))


############################
print("\nSecuencia mensajes juego: ")
def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x

generador = mensaje()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))