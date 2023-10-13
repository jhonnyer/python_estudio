#Funciones dinámicas: La integración de diferentes herramientas de control de flujo, nos permite crear funciones dinámicas y flexibles. Si debemos utilizarlas varias veces, lograremos un programa más limpio y sencillo de mantener, evitando repeticiones de código.
#Funciones
#Loops (For/While)
#Estructuras condicionales
#Palabras clave (Return, Break, Pass, Continue)

print("Ejemplo funcion que verifica si un numero esta en un rango de numeros indicado")
def chequear_tres_cifras(numero):
    return numero in range(100,1000)

resultado=chequear_tres_cifras(659)
print(f"{resultado}\n")
suma=569+123
resultado=chequear_tres_cifras(suma)
print(f"{resultado}\n")

#############################################################################
print("Funcion que recorre una lista y verifica si cada elemento de la lista esta en un rango entre 100 y 1000")
def chequear_tres_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            print("El valor: "+str(n)+ " esta en el rango entre 100 y 1000")
            return  True  #Return aqui funciona como un elemento de corte en la funcion, si se retorna un valor se sale del bucle y termina la funcion
        else:
            print("El valor: " + str(n)+" no se encuentra en el rango indicado")
            pass #Pasa a la siguiente iteracion
    return False #Si ningun elemento cumplio con la condicion

lista=[26,50,1200,123, 56]
resultado=chequear_tres_cifras(lista)
print(type(resultado))
print(resultado)
print()

lista=[26,50,1200,56]
resultado=chequear_tres_cifras(lista)
print(type(resultado))
print(resultado)
print()

#############################################################################
print("Funcion que recorre una lista y verifica si cada elemento tiene 3 cifras o esta en un rango entre 100 y 1000. Adicionalmente retorna una lista con los elementos que cumple la condicion")
def chequear_tres_cifras(lista):
    lista_3_cifras=[]
    for n in lista:
        if n in range(100,1000):
            #Almacena en la lista nueva los elementos que cumplen la condicion especificada
            lista_3_cifras.append(n)
        else:
            pass #Pasa a la siguiente iteracion
    return lista_3_cifras #Retorna la lista con los elementos que cumplen la condicion

lista=[26,50,1200,123, 56]
resultado=chequear_tres_cifras(lista)
print(type(resultado))
print(resultado)
print()

###################################
print("Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.")
def todos_positivos(lista):
    for n in lista:
        if n< 0:
            return False
        else:
            pass
    return True
lista_numeros = [10,3,-3,2]
resultado=todos_positivos(lista_numeros)
print(resultado)
print()

lista_numeros = [10,4,8,2]
resultado=todos_positivos(lista_numeros)
print(resultado)
print()

###################################
print("Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son multiplos de 2, y False si al menos uno de los valores no es multiplo de 2. Crea una lista llamada lista_numeros con valores positivos y negativos.")
def todos_positivos(lista):
    for n in lista:
        if n%2 != 0:
            return False
        else:
            pass
    return True
lista_numeros = [10,3,-3,2]
resultado=todos_positivos(lista_numeros)
print(resultado)
print()

lista_numeros = [10,4,8,2]
resultado=todos_positivos(lista_numeros)
print(resultado)
print()

###############################################################
print("Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.")
def suma_menores(lista):
    suma=0
    for n in lista:
        if n in range(0,1001):
            suma=suma+n
    return suma
lista_numeros=[-1,-3,20,54,4353,100]
resultado=suma_menores(lista_numeros)
print(resultado)
print()

##########################################
print("Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.")
def cantidad_pares(lista):
    contador=0
    for n in lista:
        if n%2 ==0:
            contador=contador+1
    return contador

lista_numeros = [-1, -3, 20, 54, 4353, 100,7,3,1,10,8,-4]
resultado=cantidad_pares(lista_numeros)
print(resultado)

#####################################
print("\nEjemplo funcion para desacoplar Tuplas, ejemplo cafe más caro")
precios_cafe=[('capuchino',1.5),('Expreso',2.3),('Moka',1.9)]
for clave, valor in precios_cafe:
    print(clave, valor)


def cafe_mas_caro(lista_precios):
    precio_mayor=0
    cafe_mas_caro=''
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor=precio
            cafe_mas_caro=cafe
        else:
            pass
    return (cafe_mas_caro, precio_mayor)
print("\nEl cafe más caro es:")
print(cafe_mas_caro(precios_cafe))
print()

print("\nEjemplo procesamiento y resultado desacoplado de una tupla: ")
cafe, precio=cafe_mas_caro(precios_cafe)
print(f"El cafe más caro es: '{cafe}' cuyo precio es: ${precio}\n")