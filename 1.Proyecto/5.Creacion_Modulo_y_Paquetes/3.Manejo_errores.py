'''
Existen estrategias para capturar y gestionar los errores que pueden presentarse al ejecutar un programa, a fines de evitar
una falla mayor y controlar la información que es mostrada al usuario.

TRY: El código que se encuentra dentro de try se ejecuta hasta finalizar o hasta que se presenta un error (excepción)

EXCEPT: Contiene el manejador de errores (respuesta del programa ante un error), atrapando las excepciones que se presentan durante la ejecución de try

ELSE:  Engloba el código que se ejecutará únicamente cuando ninguna excepción haya sido detectada en la ejecución de try (sin errores)

FINALLY: Contiene código que se ejecuta siempre, se hayan presentado o no errores

Es buena práctica capturar y manejar las excepciones posibles individualmente y brindar información acerca del error y su posible solución
'''

print("Manejor de errores TRY EXCEPT\n")
def suma(n1,n2):
    resultado=n1+n2
    print("El resultado de la suma es: "+resultado)  #Error de tipo TypeError, no se puede concactenar un string y un entero
    #print(f"El resultado de la suma es: {resultado}")

try:
    #Código que queremos probar
    n1 =int(input("Ingrese el número 1: "))
    n2= int(input("Ingrese el número 1: "))
    suma(n1,n2)
#Se pueden manejar diferentes tipos de excepciones segun el objeto utilizado
except TypeError:
    #Código a ejecutar si hay un error de tipo TypeError (No se puede concatenar un string y un entero)
    print("Estas intentando concatenar tipos de valores distintos")
except ValueError:
    #Código a ejecutar si hay un error de tipo ValueError (No es numerico en este caso)
    print("Los valores ingresados no son correctos, ingreso un número")
else:
    #Código a ejecitar si no hay un error
    print("Hiciste todo bien")
finally:
    #Código que se va a ejecutar de todos modos
    print("Fin del programa")

##################################################################################
########################  EJEMPLO 2, PEDIR NÜMERO   ##############################
##################################################################################
print("\nEjemplo 2, pedir un número correcto: ")

def pedir_numero():
    while True:
        try:
            numero= int(input("Ingresa un número: "))
        except:
            print("El dato ingresado no es de tipo numérico")
        else:
            print(f"Ingresastes el número {numero}")
            break #Finalizar el bucle While cuando se cumple la condición
        #La opción finally no es obligatoria

    print("Fin del programa, gracias")

pedir_numero()


print("\nEjemplo colocando el Manejo de Errores en una funcion")

def suma(num1, num2):
    print(num1 + num2)

def verificador_errores(n1, n2):
    try:
        n1=int(n1)
        n2=int(n2)
        suma(n1,n2)
    except:
        print("Error inesperado")
    else:
        print("Hiciste todo bien")


n1 =input("Ingrese el número 1: ")
n2= input("Ingrese el número 2: ")
verificador_errores(n1,n2)


##########################
print("\nEjemplo funcion cociente con manejo de errores: ")
def cociente(num1, num2):
    try:
        result = num1 / num2
        print(result)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

# Ejemplos de uso:

# Intenta dividir 5 por "2" (esto generará un TypeError)
cociente(5, "2")

# Intenta dividir 10 por 0 (esto generará un ZeroDivisionError)
cociente(10, 0)

# Divide 8 por 4 (esto no generará errores)
cociente(8, 4)


########################
print("\nEjemplo manejo de errores abriendo archivos: ")
def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
        archivo.close()
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

abrir_archivo("open.txt")