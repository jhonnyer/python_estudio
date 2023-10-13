#Los string son INMUTABLES, no se puede cambiar su orden interno ni cambiarlo.
#En este caso la variable texto no puede modificarse, si se desea utilizar replace se deberia crear una variable nueva para almacenar su valor
texto="Hola mundo";
texto.replace("Hola","Adios");
print("Texto inmutable: "+texto);
print("Nueva variable: "+texto.replace("Hola","Adios")+"\n");

#Ejemplo de inmutabilidad, en este caso sale un error porque ya se dijo que los tring son inmutables no puede cambiarse el orden o el caracter
#nombre="Carina";
#nombre[0]="K";
#print(nombre);

#No obstante, se puede rescribir el contenido de la variable porque si se puede variar.
nombre="Carina";
nombre="Karina"
print(nombre);

#Concatenable, se pueden concatenar, es decir unir textos de string.
texto1="Hola ";
texto2="mundo";
print(texto1+texto2+"\n");

#multilineales
texto="Hola \nmundo\n";
print(texto);

#Utilizar 3 comillas se pueden hacer salto de linea
texto="""Mil pequeños peces blancos
como si hirviera
    el color del agua.\n""";
print(texto+"\n");
#print("agua"in texto+"\n");

#Verificar si contiene un texto, palabra o letra en el string, esto retorna un booleana True o False

mi_texto="Hola mundo";
print("Hola"in mi_texto);
print("Holas"in mi_texto+"\n");

texto="""Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print("\nVerifica si la palabra agua no se encuentra en el texto mediante condición not in")
print("agua" not in texto+"\n");

#Calcular el largo de un string, cuantos caracteres posee
print("\nVerificar longitud del texto")
print(len(mi_texto));
print("");

#Multiplicar los string, en este caso el valor de la variable text se repite 3 veces.
text="Jhonnyer ";
print(text*3+"\n");