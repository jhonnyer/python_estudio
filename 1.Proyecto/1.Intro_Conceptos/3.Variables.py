#Las variables pueden cambiar su contenido en el transcurso del recorrido de la aplicación
#Reglas para nombres de las variables
#Las variables deben ser legibles, si contiene dos palabras deben estar separadas por una raya al piso (nombre_animal)
#Las variables deben empezar con una letra y no empezar por números.
#Las variables no deben contener caracteres especiales ni tildes o letras ñ
#Las variables no deben tener signos
#Las variables no pueden ser nombradas con palabras reservadas en python.
#Para ver el tipo de dato de una variable podemos utilizar la funcion type(nombre_variable)

nombre ="juan";
print("El nombre es: "+nombre);

nombre="Valentina";
print("El nombre es: "+nombre);

edad =30;
#funcion str permite parsear un dato numérico o flotante en un string;
print("El usuario ingresado es: "+nombre+" y tiene una edad de: "+str(edad));

nombre=input("Ingresa tu nombre: ");
print("El usuario ingresado es: "+nombre);

#Concatenación:
dato1 = "Hola ";
dato2 = "Python"
frase = dato1+dato2;
print(frase);

numero1= 10;
numero2= 20;
suma= numero1+numero2;
print("El resultado de la suma de: "+str(numero1)+" + "+str(numero2)+" es igual a: "+str(suma));
print(numero1+numero2);

num1=10;
num2=3.5;
resultado=num1+num2;
print(resultado);
print("La variable num1 es de tipo: "+str(type(num1))+ ". La variable num2 es de tipo: "+str(type(num2)));
print("La variable resultado producto de la suma de un entero y un flotante es de tipo: "+str(type(resultado)));


num1=3.5;
num2=3.5;
resul=num1+num2;
print(resul);
print("La variable num1 es de tipo: "+str(type(num1))+ ". La variable num2 es de tipo: "+str(type(num2)));
print("La variable resultado producto de la suma de dos flotantes es de tipo: "+str(type(resul)));

#Parsear un string a un entero, en este caso los datos recuperados de una funcion INPUT son de tipo string.
#Para parsear un string a un entero se utiliza la funcion INT(nombre_variable);
print("\nParseo Integer")
edad = input("Cual es tu edad? ");
nueva_edad=10+int(edad);
print(edad);
print(nueva_edad);

#Parsear un string o integer a flotante
print("\nParseo Flotante")
edad=12;
newEdad=float(edad);
print(newEdad);
print(type(newEdad));

#Parseo de flotante a un entero, en este caso elimina los datos decimales
print("\nParseo de flotante a un entero")
edad=5.6;
newEdad=int(edad);
print(newEdad);
print(type(newEdad));


#Formateo de cadenas dos tipos utilizando funcion format o utilizando f antes del texto string.
#Format permite manejar cualquier tipo de dato sin necesidad de indicar el tipo de dato

color_auto="Azul";
matricula=1232;
print("Mi auto es {} y de matrícula {}".format(color_auto,matricula));

#Formateo mediante cadenas literales
print(f"Mi auto es {color_auto} y de matrícula {matricula}");

#Formateo y concatenacion de enteros y resultado de una suma sin crear una nueva variable
x=10
y=5
print("La suma de {} y {} es igual a {}".format(x,y,x+y));