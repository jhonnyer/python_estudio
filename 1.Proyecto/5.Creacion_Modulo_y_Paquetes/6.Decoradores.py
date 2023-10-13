'''
Los decoradores son patrones de diseño en Python utilizados para dar nueva funcionalidad a objetos (funciones),
modificando su comportamiento sin alterar su estructura: son funciones que modifican funciones.

Las funciones en Python soportan operaciones tales como ser asignadas a una variable, pasadas como argumento, y ser devueltas por otra función como resultado.
También, es posible definir funciones dentro de funciones, sin que estén disponibles fuera de la función dentro de la cual fueron definidas.
Los decoradores permiten que una función se modifique ante determinados escenarios, sin duplicar código.

Los decoradores permite eliminar código duplicado
Se pueden aplicar los decoradores, debido a que en python todo es un objeto, incluido las funciones
'''

print("EJEMPLO 1. FUNCION DECORADA ")
def mostrar_informacion(funcion):                        #Función como parámetro de una función
    def interior():                                      #Definición de una función dentro de otra
        print(f'Ejecutando la función {funcion.__name__}')
        funcion()
        print('Ejecución finalizada')
    return interior                                      #Función que devuelve otra función como resultado

def impresion():
    print("Hola Mundo")

funcion_decorada = mostrar_informacion(impresion)       #Se asigna una función a una variable
funcion_decorada()                                      #jecución de función decorada




#############################################################
print("\nEJEMPLO 2. FUNCION DECORADA PARA FUNCION DE CONVERSION LETRAS EN MAYUSCULA Y MINUSCULA: ")
def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

print("Como en Python todo es un objeto, incluida las funciones, puedo asignar una funcion como contenido a una variable o como argumento a otra función: \n")
mi_funcion=mayuscula
mi_funcion('Python')

def procesar_funcion(funcion):
    return funcion

procesar_funcion(mi_funcion('Probando'))

print("\nEn Python puedo definir funciones dentro de otras funciones utilizando los conceptos anteriores de la siguiente forma: \n")

def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo=='may':
        return mayuscula
    elif tipo=='min':
        return minuscula

operacion1=cambiar_letras('may')
operacion1('funcion en mayuscula')

operacion2=cambiar_letras('min')
operacion2('funcion en minuscula\n')

#################################################################
print("\nEjemplo 3 funcion decorada para saludar utilizando decorador @nombre_decorador: \n")

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print('Adios')
    return otra_funcion

@decorar_saludo
def mayusculas(texto):
    print(texto.upper())
@decorar_saludo
def minusculas(texto):
    print(texto.lower())

print("Utiliza funcion decorada anterior utilizando el decorador => '@decorar_saludo' para las funciones mayusculas() y minusculas()")

minusculas('soy un texto en minuscula')
print()
mayusculas('soy un texto en mayuscula')

######################################################
#################################################################
print("\nEjemplo 3 funcion decorada para saludar pasando una funcion como decorador y capturando su contenido en una variable:")

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print('Adios')
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())
def minusculas(texto):
    print(texto.lower())

print("Pasar las funcines mayusculas() y minusculas() al decorador como parametro y capturar su contenido en una variable")

minuscula_decorada=decorar_saludo(minusculas('soy un texto en minuscula'))
print()
mayuscula_decorada=decorar_saludo(mayusculas('soy un texto en mayuscula'))
