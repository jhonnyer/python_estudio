#Es un bucle que se repite mientras se cumple una condición
#While una_condición. Puede existir un else para realizar otra acción cuando la condición no se cumpla
#Tener cuidado no se vaya a hacer un bucle infinito, se debe garantizar que el bucle llegue a una condicion que se detenga el bucle

#Instrucciones:
#Break, interrumpe el bucle y lo termina
#Pass, es una instruccion que hace que se salte el codigo y pase a la siguiente ejecución y no haga nada. Permite reservar un espacio en el ordenador
#Continue, detiene o interrumple el codigo cuando se cumple la condición, pero hace que continue en la siguiente iteración

#EJEMPLO BUCLE INFINITO, en este caso el bucle se repite infinitamente porque la condicion siempre se va a cumplir, tener cuidado
#monedas =5
#while monedas >0:
#    print(f"Tengo {monedas} monedas")

#EJemplo bucle
print("Ejemplo bucle While reduciendo la cantidad de monedad en la condición")
monedas =5
while monedas >0:
    print(f"Tengo {monedas} monedas")
    #monedas=monedas-1
    monedas-=1


#EJemplo bucle con opcion ELSE
print("Ejemplo bucle While reduciendo la cantidad de monedad en la condición y uso de un ELSE cuando la condicion no se cumple")
monedas =5
while monedas >0:
    print(f"Tengo {monedas} monedas")
    monedas-=1
else:
    print("\nNo tengo más dinero")


#EJemplo bucle While usando un string
print("\nEjemplo bucle While usando un string ingresado por teclado")
respuesta ='s'
while respuesta == 's':
    respuesta=input("Quieres continuar con la aplicación ? (s/n): ")
else:
    print("\nGracias, hasta luego")
print("FIN ")

#Ejemplo instrucción pass
opcion = 's'
while opcion == 's':
    print(opcion);
    pass
    opcion="a"
    print(opcion);

print("\nSiguiente bloque de código\n")


#Ejemplo instrucción break en un for
nombre = input("Ingresa tu nombre: ")
for letra in nombre:
    if letra == 'r':
        break
    print(letra)
print("Fin break en bucle for\n")

#Ejemplo instrucción break en un while
print("\nEjemplo instrucción break en bucle while")
contador=5
while contador>0:
    print(contador)
    if contador == 2:
        print(f"Bucle detenido en el contador número: {contador}")
        break
    contador -=1
print("Fin break en bucle while\n")


#Ejemplo instrucción continue en un for
nombre = input("Ingresa tu nombre: ")
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)
print("Fin continue en bucle for\n")


#Ejemplo instrucción continue en un while
print("\nEjemplo instrucción continue en bucle while")
contador=5
while contador>0:
    contador -= 1
    if contador == 2:
        continue
    print(contador)
print("Fin continue en bucle while\n")

#Ejemplo instrucción continue en un while
print("\nEjemplo instrucción continue en bucle while")
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        print("Este es el contador 3, se salta esta iteración.")
        continue
    print(f"Contador: {contador}")


#Ejemplo while contador
print("\nEjemplo while contador del 10 al 0")
numero = 10
while numero >=0:
    print(numero)
    numero-=1

#Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:
#- Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)
#- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).
print("\nEjemplo while contador del 50 al 0 verificando numeros divisibles por 5")
numero = 50
while numero>=0:
    if numero % 5 ==0:
        print(numero)
    numero -=1

#Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo
print("\nEjemplo while en lista saltando números negativos")
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for element in lista_numeros:
    if element < 0:
        break
    print(element)