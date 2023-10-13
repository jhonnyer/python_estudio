'''
El módulo math contiene un conjunto de métodos y constantes que se pueden utilizar para resolver tareas
matemáticas de mayor complejidad. Es el equivalente a la calculadora científica dentro de Python

Algunas de las situaciones que pueden ayudarnos a resolver son:

* Relaciones trigonométricas (seno, coseno, tangente, sus inversas e hiperbólicas)
* Funciones logarítmicas
* Potencias y raíces
* Combinatoria y permutaciones
* Redondeos
* Factoriales

entre muchas otras.

Constantente:

* Pi (3.1415...)
* e o Constante de Euler (2.7182...)
* Tau (6.2831...)
* Infinito (el concepto matemático de infinito positivo)
* Nulo (NaN: not-a-number)
'''

import math
print("Euler => math.e")
resultado = math.e
print(resultado)

print("\nConstante PI => math.pi")
resultado = math.pi
print(resultado)


print("\nRedondeo hacia abajo => math.floor(89.665)")
resultado = math.floor(89.665)
print(resultado)

print("\nRedondeo hacia arriba => math.ceil(89.665)")
resultado = math.ceil(89.665)
print(resultado)


print("\nFunción logaritmo => math.log(100,5)  => Donde 100 es el numero y 5 la base")
resultado = math.log(100,5)
print(resultado)
resultado = math.log(25,5)  #=> 5*5 =25
print(resultado)

print("\nLogaritmo en base 10 de 25 => math.log10(25)")
resultado=math.log10(25)
print(resultado)

print("\nFunción tangente => math.tan(2565)")
resultado = math.tan(2565)
print(resultado)


print("\nFunción coseno => math.cos(2565)")
resultado = math.cos(2565)
print(resultado)

print("\nFunción seno => math.sin(2565)")
resultado = math.sin(2565)
print(resultado)

print("\nRaiz cuadrada ")
# Obtener la raíz cuadrada de pi
resultado = math.sqrt(math.pi)
# Imprimir el resultado
print("La raíz cuadrada de π (pi) es:", resultado)


print("\nProducto Factorial: ")
# Calcular el factorial de 7
resultado = math.factorial(7)
# Imprimir el resultado
print("El factorial de 7 es:", resultado)
