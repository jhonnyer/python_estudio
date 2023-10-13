''' MEDIR EL TIEMPO
Estudiar el tiempo transcurrido durante la ejecución de un código nos permite conocerlo mejor y tomar decisiones acerca
de la vía más eficiete para resolver un problema. Tenemos dos módulos que nos ayudarán: time y timeit.

* Utilizando time, para funciones que toman varios segundos para ejecutarse:
        inicio = time.time()
        [código]
        final = time.time()
        duracion = final - inicio

* utilizando timeit:
        duracion = timeit.timeit(declaracion, setup, number = numero)

 - declaracion: recibe el código que cuya duración de ejecución queremos medir => Invocacion de mi funcion
 - setup: recibe las instrucciones que el parámetro declaracion requiere para funcionar  => Definicion de la funcion
 - number: cantidad de veces que se evaluará el código para obtener su tiempo de ejecución mínimo. => pueden ser varios miles o cientos de veces (dependiendo de la complejidad)
'''
import time, timeit
print("Vamos a probar el tiempo que demora en ejecutar dos funciones que hacen lo mismo, pero con diferente implementación: ")
def prueba_for(numero):
    lista=[]
    for num in range(1,numero+1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista=[]
    contador=1
    while contador<=numero:
        lista.append(contador)
        contador +=1
    return lista

print("\nProbar eficacia de cada funcion: ")
print("Función prueba_for(): ")
inicio=time.time()
print(prueba_for(10000))
final=time.time()
result1=final-inicio
print(result1)

print("\nFunción prueba_while(): ")
inicio=time.time()
print(prueba_while(10000))
final=time.time()
result2=final-inicio
print(result2)
if result1> result2:
    print("Función prueba_for() es más eficiente")
else:
    print("Función prueba_while() es más eficiente")

print("\nPara intervalos pequeños, time no es muy preciso ya que no toma valores minimos, por lo tanto se recomienda utilizar timeit. ")
print("Estructura timeit() =>  declaracion, mi_setup, numeros_veces_repetir")
print("Funcion prueba_for()")
declaracion='''
prueba_for(10)
'''

mi_setup='''
def prueba_for(numero):
    lista=[]
    for num in range(1,numero+1):
        lista.append(num)
    return lista
'''
duracion1=timeit.timeit(declaracion,mi_setup,number=1000000)
print(duracion1)

####################################################
print("\nFuncion prueba_while()")
declaracion='''
prueba_while(10)
'''

mi_setup='''
def prueba_while(numero):
    lista=[]
    contador=1
    while contador<=numero:
        lista.append(contador)
        contador +=1
    return lista
'''
duracion2=timeit.timeit(declaracion,mi_setup,number=1000000)
print(duracion2)
if duracion1> duracion2:
    print("Función prueba_for() es más eficiente")
else:
    print("Función prueba_while() es más eficiente")