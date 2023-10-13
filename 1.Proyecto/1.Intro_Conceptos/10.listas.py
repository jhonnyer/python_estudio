#Lista es una secuencia ordenada de objeto de cualquier tipo de datos. La lista se define en corchetes
#Las listas no son inmutables por lo cual se puede modificar su contenido, se pueden ordenar o hacerle slicing.

numeros=[10,20,30,40,50];
print(type(numeros));  #Tipo de dato una clase list
print(numeros[0]); #Indexar la lista, es decir extraer el dato que se encuentra en la posicion 0 de la lista
print(numeros[1:3]);  #Slicing de la lista, en este caso los objetos de la lista desde la posicion 0 hasta la 3, sin incluir la posicion 3, igual que en los string
print();

lista1=["a","b", 12, 12, 13, 14, 15.4, "fin"];
print(lista1);

print(len(lista1)); #Longitud de la lista
print(type(lista1));
print();

#Concatenacion de listas
print("Concatenación de listas")
lista1=["a","b","c"];
lista2=[1,2,3,4,5,6,7,8];
resultado=lista1+lista2;
print(resultado);
print()

#Slicing lista ejemplo
print("Ejemplo slicing lista desde posicion 2 hasta el final, funciona igual que el string")
print(lista2[2:])
print()
print("Ejemplo slicing, lista al revez")
print(lista2[::-1]);
print();
print("Ejemplo slicing ultimo dato");
print(lista2[-1]);
print();

#Modificar un elemento de la lista, prueba no inmutable
print("Verificación que la lista no es inmutable, añadir un nuevo elemento a la lista");
lista2.append("fin");
print(lista2);
print();

print("Eliminar un elemento de la lista, en este caso el metodo pop elimina el ultimo elemento")
lista2.pop();
print(lista2)
print();

print("Eliminar un elemento de la lista, en este caso al metodo pop le indicamos que elemento en que indice (indice 2) eliminar")
lista2.pop(2); #Quitamos el elemento en el indice 2 correspondiente al numero 3.
print(lista2)
print();

#El elemento eliminado se puede guardar en una variable
print("Guardar el elemento eliminado en una variable")
elemento=lista2.pop(6);
print(f"El elemento eliminado es: {elemento} \n");

#Ordenamiento de lista por orden alfabetico y numerico
lista=["z", "g", "a", "d", "b", "v"]
print("Ordenar lista orden alfabetico");
lista.sort();
print(lista);
print();

print("Ordenar lista orden numerico");
lista=[5,1,8,4,6,3,2,7];
lista.sort(); #Sort es un metodo que realiza una acción pero que  no retorna nada por lo tanto no se puede crear una nueva variable a partir de este metodo, retorna un noneType
print(lista);
print();

#Sort es un metodo que realiza una acción pero que  no retorna nada por lo tanto no se puede crear una nueva variable a partir de este metodo, retorna un noneType
lista=[5,1,8,4,6,3,2,7];
print("Verificacion metodo sort el cual realiza una acción pero no retorna nada, por lo cual no se puede asignar a una nueva variable ya que retorna nada. La nueva variable por lo tanto sera de tipo NoneType")
new_lista=lista.sort();
print(new_lista);
print(type(new_lista));
print();

#Si quiere ordenarla y luego almacenar en otra variable debo ordenarla  y esa lista ordenada se la paso a otra variable
print("Crear una nueva lista a partir de una lista ordenada");
lista=[5,1,8,4,6,3,2,7];
lista.sort();
new_lista=lista
print(new_lista);
print(type(new_lista));
print();

#Metodo reverse permite realizar una inversion del orden de la lista, pone el ultimo elemento de primero y asi, este metodo no retorna nada
lista=[5,1,8,4,6,3,2,7];
lista.reverse();
print("Metodo reverse, el cual pone el ultimo elemento de primero y asi sucesivamente, este método no retorna nada");
print(lista);
print();

#Cambiar un valor de un indice en la lista
print("Cambiar un valor de un indice en la lista, en este caso la posicion 3 que tiene el valor 6 se cambia por el string 'Valor cambiado'");
lista[3]="Valor cambiado";
lista[2]=True;
print(lista)
print();