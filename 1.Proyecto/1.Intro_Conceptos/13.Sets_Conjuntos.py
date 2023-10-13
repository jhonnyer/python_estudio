#sets o conjuntos:  Los sets son otro tipo de estructuras de datos. Se diferencian de listas, tuplas y diccionarios
# porque son una colección mutable de elementos inmutables, no ordenados y sin datos repetidos.
#Si se añade elementos repetidos dentro de un set, el set automaticamente elimina los duplicados
#Como no son ordenados, no se pueden indexar

#Conjunto instanciado entre corchetes
conjunto1=set([1,2,3,4,5,6]);
print(conjunto1);
print(type(conjunto1));
print()

#Conjunto instanciado entre parentesis
conjunto1=set((1,2,3,4,5,6));
print(conjunto1);
print(type(conjunto1));
print()

#Conjunto instanciado con datos duplicados (el valor 1), en este caso se elimina el valor 1
print("Set con asignacion de elementos duplicados")
conjunto2={1,2,3,4,5,'fin',True,1,1,1};
print(conjunto2);
print(type(conjunto2));
print()

#Los objetos set no son indexables por lo tanto conjunto2[1] no se puede.
#Los objetos de tipo lista no pueden ser instanciados dentro de un set.
#No obstane, los set si admiten tuplas
print("Set con asignacion de lista no se puede, sin embargo si admiten tuplas porque sus datos son inmutables")
#conjunto3={1,2,3,4,5,'fin',True,1,1,[4,5]};
conjunto3={1,2,3,4,5,'fin',True,1,1,(1,4,5)};
print(type(conjunto3));
print(conjunto3);
print()

print("Funcion len en set")
print(len(conjunto3));
print();

print("Verificar si un valor existe o no en un set con in o not in")
print(2 in conjunto3);
print(2 not in conjunto3);
print(8 not in conjunto3);
print()

#Unión de set
print("Unión de set");
s1={1,2,3};
s2={3,4,5};
s3=s1.union(s2);
print(s3);
print();

#Añadir un elemento al set
print("Añadir un elemento al set con metodo add()");
s1={1,2,3};
s1.add(False);
s1.add(4);
s1.add(2); #No añade un valor que ya existe
print(s1);
print();


#Remover un elemento al set
print("Remover un elemento al set con metodo remove()");
s1.remove(3)
print(s1);
#s1.remove(3); #Si intento eliminar un elemento que no existe en el set sale error;
print();

#Remover un elemento al set mediante metodo Discard
print("Remover un elemento al set con metodo discard() el cual funciona igual que el metodo remove, sin embargo, si un elemento no existe no genera error");
s1.add(3);
s1.discard(3)
s1.discard(3)
print(s1);
#s1.remove(3); #Si intento eliminar un elemento que no existe en el set sale error;
print();

#Remover un elemento al set mediante metodo pop()
print("Remover un elemento al set con metodo pop() el cual remueve objetos del conjunto de forma aleatoria, tener en cuenta esto. El método pop retorna el valor eliminado y puede almacenarse en una variable");
eliminado=s1.pop();
print(s1);
print(f"Elemento eliminado: {eliminado}");
print();

#Limpiar el conjunto
print("Limpiar o vaciar todos los datos del conjunto con el método clear")
s1.clear()
print(s1)
print()

print("Existen muchos mas métodos de manejo de conjuntos en la documentación de sets.")


