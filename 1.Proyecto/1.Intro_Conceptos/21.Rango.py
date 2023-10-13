#Rango, permite generar un rango de numeros desde 0 o un valor definifico, hasta x valor indicado como parametro sin necesidad de generar una lista
#Rango permite 3 parametros: Primero, define el inicio del rango, Segundo: Hasta donde, Tercero: Pasos o saltos para generar el rango

lista=range(5)
print(lista)
for num in lista:
    print(num)

#for utilizando un rango
print("\nFor utilizando un rango")
for num in range(5):
    print(num)


#Rango de datos desde el 2 hasta el 10
#NOTA: El ultimo valor no se incluye en el rango, en este caso el número 10, si quiero incluirlo debo hacer el rango hasta el 11.
print("\nFor utilizando un rango desde 2 hasta 10 => range(2,10)")
for num in range(2,10):
    print(num)

#Rango de datos desde el 2 hasta el 10 saltando de paso en paso definido como tercer parametro.
#NOTA: El ultimo valor no se incluye en el rango, en este caso el número 10, si quiero incluirlo debo hacer el rango hasta el 11.
print("\nFor utilizando un rango desde 2 hasta 20, saltando de 2 en 2 => range(2,20,2)")
for num in range(2,20,2):
    print(num)

#Ejemplo crear una lista desde el 1 hasta el 100 utilizando el casteo de una lista con el metodo list.
#Se coloca la lista hasta el 101 porque acordemosnos que el ultimo número no se incluye
print("\nCrear una lista desde 1 hasta el 100 utilizando metodo list y range => list(range(1,101))")
lista=list(range(1,101))
print(lista)
print()
mi_lista = list(range(2500,2586))
print(mi_lista)
print()

#Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.
mi_lista = list(range(3, 301, 3))
print(mi_lista)
print()

#Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.
#Crea un rango de valores que puedas recorrer en un loop
#Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).
#Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.
print("Crear un rango de valores del 1 al 15 y sumar todos sus cuadrados y mostrar el resultado final")
suma_cuadrados = 0
for element in range(1,16):
    cuadrado=element**2
    suma_cuadrados=suma_cuadrados+cuadrado
    print(f"Suma parcial: {suma_cuadrados}")

print(suma_cuadrados);