#Método Index => Permite conocer el indice de un caracter.
#Cada letra dentro de una palabra en python ocupa un espacio en memoria definido por un indice, ejemplo:
#Palabra "HOLA"; en este caso la H tiene el indice 0, la O indice 1, la L indice 2 y la A el indice 3.

#Utilizamos el método index( ) para explorar strings, ya que permite hallar el índice de aparición de un caracter o cadena de caracteres dentro de un texto dado.

#Los indices positivos empiezan desde la posición 0 de izquierda a derecha
mi_texto="Esta es una prueba de indice";
print(mi_texto+"\n");
#Obtener el caracter que ocupa la posición 3.
resultado= mi_texto[3];
print("Resultado busqueda caracter en la posición 3 es "+resultado);

resultado= mi_texto[-4];
#Los indices negativos empiezan desde la posición -1 de derecha a izquierda
print("Resultado busqueda caracter en la posición -4 es "+resultado);

#Método index, encuentra la primer posición en que se encuentra el caracter 'a' de izquierda a derecha.
print("\nMétodo index busqueda por una letra en especifico");
resultado=mi_texto.index("a");
print(resultado)

#En este caso se busca el indice donde esta ubicado o empieza la palabra 'prueba'.
print("\nMétodo index busqueda por una palabra en especifico");
resultado=mi_texto.index("prueba");
print(resultado)

#NOTA: Si la letra o palabra no esta, se lanza una excepcion, es importante tener en cuenta que el codigo detecta entre mayusculas y minusculas.

#Método index, podemos indicarle donde empiece o termine la busqueda desde un indice en especifico.
print("\nMétodo index busqueda por una letra a partir del caracter 5");
resultado=mi_texto.index("a",5);
print(resultado)

#En este caso, marcaria un error porque el indice 10 no es inclusivo, se busca hasta antes del indice 10, si queremos incluirlo se debe añadir hasta el indice 11.
print("\nMétodo index busqueda por una letra a partir del caracter 5 hasta el indice 10");
#resultado=mi_texto.index("a",5,10);
resultado=mi_texto.index("a",5,11);
print(resultado)


#Método RINDEX realiza la busqueda al revez, de derecha a izquierda.
print("\nMétodo RINDEX busqueda por una letra");
resultado=mi_texto.rindex("a");
print(resultado)
