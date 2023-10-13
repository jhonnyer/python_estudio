#La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
#algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
#para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
#número y el programa puede responder cuatro cosas distintas:
#* Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
#un número que no está permitido.
#* Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
#decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
#* Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
#misma manera.
#* Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
#intentos le ha tomado.
#Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
#número. Y así hasta que gane o hasta que se agoten los ocho intentos.
#

from  random import  randint;
intentos=0
estimado=0
numero_secreto= randint(1,100)
nombre=input("Digita tu nombre: ")

print(f"""Bueno, {nombre}, he pensado un número entre 1 y 100. 
Tienes solo ocho intentos para adivinar cuál crees que es el número""")

while intentos<8:
    intentos +=1
    estimado = int(input("¿Cuá el es el número secreto? "))
    #if estimado <1 or estimado >100:
    if estimado not in range(1,101):  #Mejora codigo
        print("Has elegido un número que no está permitido")
    elif estimado < numero_secreto:
        print("Su respuesta es incorrecta, has elegido un número menor al número secreto")
    elif estimado > numero_secreto:
        print("Su respuesta es incorrecta, has elegido un número mayor al número secreto")
    else:
        print(f"Felicitaciones {nombre}, el número secreto es: {numero_secreto},  has adivinado en {intentos} intentos")
        break;
if estimado != numero_secreto:
    print(f"Lo siento, se han acabado todos los intentos, el número secreto era: {numero_secreto}")