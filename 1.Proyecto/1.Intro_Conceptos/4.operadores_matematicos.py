x=6;
y=2;
z=7;

print(f"{x} + {y} = {x+y}");
print(f"{x} - {y} = {x-y}");
print(f"{x} * {y} = {x*y}");
print(f"{x} / {y} = {x/y}");

#Division al piso, elimina los decimales que pueda tener la división
print(f"{z} dividido al piso de {y} es igual {x//y}");

#Modulo, lo restante de una división, por ejemplo 7/2 sobra uno, y ese es el valor del modulo
#El modulo se utiliza en programacion para saber cuando un numero es par
print(f"{z} módulo de {y} es igual a {z%y}");
print(f"{x} elevado a la {y} es igual a {x**y}");
print(f"{x} elevalo a la  {3} es igual a {x**3}");
print(f"La raíz cuadrada de {x} es {x**0.5}");

#Redonde de números decimales utilizando funcion ROUND
#Round recibe dos parametros, el número a redondear y los decimales a mostrar, si no se define los decimales se redondea a un entero segun el valor mas cercano por ejemplo 5.3 se redondea a 5;  mientras que 5.6 a 6.
print("\nRedondeo de números decimales")
print(round(90/7));
print("\nRedondeo con dos decimales")
valor=5.67645645645323;
print(round(valor,2));
print(f"El valor a redondear {valor}, una vez redondeado a dos cifras es {round(valor,2)}; y es de tipo: {type(round(valor,2))}");