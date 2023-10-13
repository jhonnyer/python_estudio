#Tuplas son colecciones de elementos muy similares a las listas, pero con la diferencia de que son inmutables, no se pueden modificar
#Se definen igual que una lista con parentesis o sin parentesis y pueden contener cualquier tipo de dato (objeto)
#Ocupan menos espacio de memoria y son más rapidos de procesar.
#Las tuplas son indexadas, por lo cual funciona el manejo de indices
#Admite datos duplicados

mi_tupla=(1,2,3,4); #Forma de definir una tupla con parentesis
print(type(mi_tupla));
print(mi_tupla);
print()

#Dentro de las tuplas se aceptan cualquier tipo de datos, incluidas tuplas
mi_tupla=1,2,'a',True, False, 'c',(2,4); #Forma de definir una tupla sin parentesis, funciona igual
print(type(mi_tupla));
print(mi_tupla);
print()

print("Indexación de tuplas, no obstante los datos son inmutables, no aceptan asignacion de items")
print(mi_tupla[-1]);
print(mi_tupla[2]);
print(mi_tupla[6][1]);
print();

print("Convertir una tupla en una lista con el metodo list(mi_tupla)");
mi_lista=list(mi_tupla);
print(mi_lista);
print(type(mi_lista));
print();

print("Convertir una lista en una tupla con el metodo tuple(mi_lista).");
mi_tuple=tuple(mi_lista);
print(mi_tuple);
print(type(mi_tuple));
print();


print("Asignación de valores de un tupla a multiples variables, el número de variables deben coincidir con el número de elementos de la tupla");
mi_tupla=(1,2,3,4);
x,y,z,w=mi_tupla;
print(x);
print(y);
print(z);
print(w);
print(type(x));
print("La asignacion de valores tambien funciona para las listas y diccionarios siempre que coindican el número de elementos")
print();

print("Número de elementos de una tupla con el metodo len()");
mi_tupla=(1,2,3,4,1);
print(len(mi_tupla));
print("Verificación de cuantas veces aparece un elemento en la tupla con el metodo count()");
print(mi_tupla.count(1));
print("Posición de un elemento en la tupla mediante metodo index()");
print(mi_tupla.index(1));

