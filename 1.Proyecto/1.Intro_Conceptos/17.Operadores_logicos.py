#Operadores lógicos permiten tomar decisiones con base a varias condiciones
#Operador and:  a and b; en este caso la condicion es verdadadera si a y b es verdadero, si almenos una es falso la salida es falso
#Operador or:  a or b; en este caso la condicion es verdadadera si almenos la condicion a ó la condicion b es verdadero, si las dos son falso la salida es falso
#Operador not: Niega la respuesta de la condicion ejemplo not True es Falso y not False es True.
#Ejemplos

print("Ejemplo sin utilizar operador and")
mi_bool= 4<5<6;
print(mi_bool)
print()
print("Ejemplo utilizando operador and")
mi_bool= (4<5) and (5 > 6);  #Para que sea True, ambas condiciones deben ser verdaderas
print(mi_bool)
print()


print("Operador and utilizando string y enteros")
mi_bool= (4<5) and ("perro" == "perro");
print(mi_bool)
print()


print("Ejemplo sin utilizar operador or")
mi_bool= 4<5>6;
print(mi_bool)
print()

print("Ejemplo utilizando operador or")
mi_bool= (4<5) or (5 > 6);
print(mi_bool)
print()


print("Ejemplo utilizando operador or")
mi_bool= (4>5) or (5 > 6);
print(mi_bool)
print()


print("Ejemplo verificando una frase dentro de un texto con operador and")
texto= "Estra frase es breve"
mi_bool= ('frase' in texto) and ('breve' in texto);
print(mi_bool)
print()


print("Ejemplo verificando una frase dentro de un texto con operador and")
mi_bool= ('frase' in texto) and ('python' in texto);
print(mi_bool)
print()

print("Ejemplo verificando una frase dentro de un texto con operador or")
texto= "Estra frase es breve"
mi_bool= ('frase' in texto) or ('python' in texto);
print(mi_bool)
print()

print("Ejemplo verificando una frase dentro de un texto con operador or")
texto= "Estra frase es breve"
mi_bool= ('frases' in texto) or ('python' in texto);
print(mi_bool)
print()

print("Operador not, niega la respuesta de la condicion, en este caso de igualdad")
mi_bool=not('a'=='a')
print(mi_bool)
print()

print("Operador not, niega la respuesta de la condicion, en este caso de diferente")
mi_bool=not('a'!='a')
print(mi_bool)
print()

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = (palabra1 not in frase) and (palabra2 not in frase)
print(mi_bool);