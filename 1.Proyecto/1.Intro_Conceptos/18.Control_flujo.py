#Control de Flujo, permite verificar una condicion y de acuerdo a esta condicion tomar uno u otro caimino
#Las palabras utilizadas para evaluar el control de flujo son:
#IF: Verifica una condicion y retorna un booleano
#ELIF: Si una condicion anterior no se cumple, procede a verificar la condicion siguiente definida en el ELIF
#ELSE: Si las condiciones anteriores no se cumplen, ingresa a la ultima condicion que es sino.
#ES inmportante tener en cuenta que  el control de flujo debe ir identado con tabulaciones
#Despues de definir la condicion se coloca 2 puntos (:) y en la parte inferior identado el codigo a realizar

#Ejemplo condicion if TRUE
print("Ejemplo condicion IF TRUE")
if 10>9:
    print('Es correcto \n')
else:
    print("No es correcto \n")

#Ejemplo condicion if False
print("Ejemplo condicion IF FALSE")
if 10<9:
    print('Es correcto \n')
else:
    print("No es correcto \n")


#Ejemplo condicion if utilizando variable booleana
x= 10== 5*2
print("Ejemplo condicion IF utilizando variable con un resultado booleano")
if x:
    print('Es correcto \n')
else:
    print("No es correcto \n")


#Ejemplo condicion if utilizando variable booleana a partir de una comparacion de string
mascota= 'perro'
print("Ejemplo condicion IF, ELIF y ELSE utilizando una variable con un resultado booleano a partir de una comparacion de string")
if mascota == 'gato':
    print('Tu mascota es un gato \n')
elif mascota == 'perro':
    print('Tu mascota es un perro \n')
else:
    print("No tienes un animal de mascota o no se cual es \n")

#Ejemplo control flujo edad y calificacion escolar
print("Ejemplo calculo edad y calificacion")
edad=16
calificacion=3
if edad<18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("No aprobado")
else:
    print("Eres adulto")
print()

#Ejemplo con datos de entrada desde input
print("Ejemplo datos de entrada desde el input")
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2 :
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
print()

#Ejemplo licencias
print("Ejemplo licencia y edad")
edad = 16
tiene_licencia = False
if edad > 18:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
print()

#Ejemplo contratacion idioma ingles y Python
print("Ejemplo contratacion python e idioma ingles")
habla_ingles = True
sabe_python = False
if sabe_python:
    if habla_ingles:
            print("Cumples con los requisitos para postularte")
    else:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
        print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")