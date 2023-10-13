#Diccionarios, es una colección de conceptos unicos con una estructura clave-valor
#Las claves en un diccionario deben ser unicas, sin embargo el valor si puede repetirse.
#los diccionarios no tienen un orden especifico ni pueden ser indexados.
#Para acceder a un valor dentro del diccionario se realiza con base a su clave
#los valores de un diccionario pueden ser de cualquier tipo de dato entero, flotante, string, lista, otro diccionario, booleano...
#Los diccionarios son mutables, se pueden modificar
#Ejemplo:

mi_diccionario={'clave1':'valor 1', 'clave2':'valor 2', 'clave3':True, 'clave4':88, 'clave5':55.4,'clave6':[2,3,'fin'], 'clave7':{'c1':1,'c2':2}};
print(type(mi_diccionario)); #Verificar tipo de dato diccionario
print(mi_diccionario);
print("Ejemplo, acceder al valor de la clave2");
print(mi_diccionario['clave2']);
print();

print("Almacenar el valor de una clave en una variable, en este caso una lista")
resultado=mi_diccionario['clave6'];
print(resultado);
print("Almacenar el valor de una clave en una variable, en este caso una lista y a su vez acceder a un elemento especifico dentro de la lista")
resultado=mi_diccionario['clave6'][2];
print(resultado);
print("Almacenar el valor de una clave en una variable, en este caso un diccionario a su vez acceder a un elemento especifico dentro del diccionario")
resultado=mi_diccionario['clave7']['c2'];
print(resultado);
print();

print("Convertir un dato del diccionario en mayuscula utilizando metodo upper()")
dic={'c1':['a','b','c'], 'c2':['d','e','f']};
print(dic['c1'][0].upper());
print()

print("Agregar elementos a un diccionario");
dic={1:'a',2:'b'};
print(dic);
dic[3]='c';  #Añadimos un elemento con clave 3 y valor 'c' al diccionario.
print(dic);

print("Sobreescribir el valor de un elemento en  el diccionario, en este caso para la clave 2");
dic[2]='Valor cambiado';  #Añadimos un elemento con clave 3 y valor 'c' al diccionario.
print(dic);
print()

print("Conocer las claves del diccionario");
print(dic.keys());
print()

print("Conocer las valores del diccionario");
print(dic.values());
print()

print("Conocer las claves y valores del diccionario");
print(dic.items());
print();

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])
