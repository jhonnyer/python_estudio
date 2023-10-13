#Una función es un bloque de código que solamente se ejecuta cuando es llamada. Puede recibir información (en forma de parámetros), y devolver datos una vez procesados como resultado.
#una función es definida mediante la palabra clave def => def mi_funcion(argumento)
#Los argumentos contienen información que la función utiliza o transforma para devolver un resultado
#Para llamar a una función, basta utilizar su nombre, entregando los argumentos que la misma requiere entre paréntesis.  => mi_funcion(mi_argumento)
#RETURN: Para que una función pueda devolver un valor (y que pueda ser almacenado en una variable, por ejemplo), utilizamos la declaración return.
#=> def mi_funcion():
#       return [algo]
#Las funciones permiten crear bloques de código que pueden ser fácilmente ejecutados muchas veces y en distintos contextos sin necesidad de reescribir el bloque de código constantemente.
#La declaración return provoca la salida de la función. Cualquier código que se encuentre después en el bloque de la función, no se ejecutará
#La variable resultado almacenará el valor devuelto por la función mi_funcion( ) =>> resultado = mi_funcion()

print("Definición de función sin argumentos y sin retornar valores => def mi_funcion():")
def mi_funcion():
    print("Hola mundo\n")
print("Ejecutar la funcion creada invocandola => mi_funcion()")
mi_funcion()

print("Definición de función con argumentos y sin retornar valores => def mi_funcion(argumento):")
'''
    Comentarios de la funcion: 
    :param nombre: parametro de entrada
    :return:  valor retornado por la funcion
    '''
def mi_funcion(nombre):
    print(f"Hola {nombre}, bienvnido\n")
print("Ejecutar la funcion creada dos veces invocandola y pasandole el argumento requerido => mi_funcion(argumento)")
mi_funcion('Jhonnyer')
nombre='Fernando'
mi_funcion(nombre)

print("Funcion con operaciones aritméticas")
def cuadrado(un_numero):
    print(un_numero ** 2)
un_numero = 2
cuadrado(un_numero)
print()

#FUNCIONES CON VALORES DE RETURN
print("Función utilizando un return y almacenarlo en una variable")
def suma(num1,num2):
    #El bloque comentado funciona igual que hacer la operacion directamente en el return, sin embargo ocupa mas espacio de memoria
    #suma=num1+num2
    #return suma
    return  num1+num2

num1=10
num2=20
resultado=suma(num1,num2)  #Valor retornado en la funcion suma almacenado en la variable resultado
print(f"El resultado de la suma entre {num1}+{num2} es igual a: {resultado}")

#FUNCIONES CON VALORES DE RETURN
print("\nFunción utilizando un return y almacenarlo en una variable")
def suma(num1,num2):
    #El bloque comentado funciona igual que hacer la operacion directamente en el return, sin embargo ocupa mas espacio de memoria
    suma=num1+num2
    print(f"El resultado de la suma entre {num1}+{num2} es igual a: {suma}")
    return suma

num1=10
num2=20
resultado=suma(num1,num2)  #Valor retornado en la funcion suma almacenado en la variable resultado
print(resultado);
print("En este caso, la funcion recibe enteros o flotantes, sin embargo si se le pasa un string u otro dato va a falla la funcion")
print()

print("Ejemplo funcion que retorna una potencia a partir de dos argumentos")
def potencia(num1, num2):
    return num1**num2
print(potencia(3,4))
print()

print("Función conversión de dolares")
def usd_a_eur(monto_usd):
    tasa_cambio = 0.90
    monto_eur = monto_usd * tasa_cambio
    return monto_eur
# Monto en dólares que quieres convertir a euros
dolares = 100
# Llamamos a la función usd_a_eur para realizar la conversión
euros = usd_a_eur(dolares)
# Imprimimos el resultado
print(f"{dolares} USD son equivalentes a {euros} EUR.")

#Funcion conversion de caracteres, invertir palabra
print("\nFuncion conversion de caracteres, invertir palabra")
def invertir_palabra(palabra):
    palabra = palabra[::-1].upper()
    return palabra

palabra='Python'
resultado=invertir_palabra(palabra)
print(resultado)