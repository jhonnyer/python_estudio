print('''Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
Esta función va a mostrar en pantalla todos los números  primos existentes en el rango que va desde cero hasta ese  número incluido, y va a devolver la cantidad de números primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.\n''')

def numeros_primos(numero):
    primos=[2] #2 es un número primo, ya que por convención el 0 y 1 uno se consideran primos
    iteracion=3 #Empezar la iteracion desde el número 3 ya que el dos siempre iria

    if numero <2:
        return 0

    while iteracion <= numero:
        #El siguiente bucle lo ejecutamos que salte de 2 en 2 porque sabemos que cada número par no es un número primo
        # si iteracion es divisible por n usando el operador de módulo (%). Si iteracion es divisible por n, entonces no es un número primo, y se incrementa iteracion en 2 (para pasar al siguiente número impar) y se rompe el bucle for con la instrucción break.
        for n in range(3,iteracion,2):
            #Dividimos cada valor de la iteracion con sus valores anteriores, si el modulo es igual a cero no es un primo, pero si es diferente a cero en este caso 1 es primo
            if iteracion % n ==0:
                iteracion+=2
                break
        else:
            # Si iteracion no es divisible por un valor anterior, entonces es considerado un número primo y se agrega a la lista
            primos.append(iteracion)
            iteracion+=2
    print(primos)
    return len(primos)

print(f"Número de primos encontrados: {numeros_primos(50)}")
print()

#Un número primo unicamente cumple con la condicion que sea divisible por si mismo o por la unidad
numero=20
iteracion=3
lista=[2]
while iteracion <= numero:
    for n in range(3, iteracion, 2):
        print("n: {} .iteracion: {}.  Modulo: {}".format(n,iteracion, iteracion % n))
        if iteracion % n == 0:
            print("El número {} no es número primo \n".format(iteracion))
            iteracion += 2
            break
    else:
        # Tres es un número primo, un número primo unicamente cumple con la condicion que sea divisible por si mismo o por la unidad
        #Si iteracion no es divisible por un valor anterior, entonces es considerado un número primo y se agrega a la lista
        print("PRIMO " + str(iteracion)+"\n")
        lista.append(iteracion)
        iteracion += 2


print(lista)