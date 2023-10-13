#Metodos: Son funciones de los objetos que permiten manipularlos, analizarlos y ejecutar acciones
#Los metodos son funciones creadas por Python y que fueron incorporados por ellos a los objetos.
#Ejemplo el metodo index de string que nos permite acceder a informacion del objeto y analizarlo
#Todos los objetos tienen diferentes metodo ya definidos

print("Ejemplo metodo popitem() predifinido en un diccionario")

dic={'clave1':100, 'clave2':500}
retorno=dic.popitem() #Metodo que remueve un elemento en el diccionario y retorna el elemento eliminado
print(retorno)
print("Diccionario sin el elemento eliminado")
print(dic)

#Manejo de texto
print("\nMétodos para manejo de string en el siguiente texto: \n")
texto=",:_#,,,,,,:::____##Pyt%on_ _\nTotal,,,,,,::#"
print(texto)
print()
print("\nUtilización método lstrip para eliminar caracteres en un texto de izquierda a derecha")
caracteres_a_eliminar = ",:_#%_"
resultado = texto.lstrip(caracteres_a_eliminar)
print(resultado)

print("\nUtilización método rstrip para eliminar caracteres en un texto de derecha a izquierda")
caracteres_a_eliminar = ",::#"
resultado = resultado.rstrip(caracteres_a_eliminar)
print(resultado)

print("\nUtilización método replace para eliminar salto de línea y cambiar el simbolo del % en la palabra 'Pyt%on' por h")
resultado = resultado.replace("\n",'').replace('%','h').replace("_", "")
print(resultado+"\n")

print("Eliminar salto de linea al final de la siguiente cadena impresa en pantalla y cambiar la palabra 'con' a la palabra 'sin'")
cadena_con_salto = "Esta es una cadena con un salto de línea al final.\n"
print(cadena_con_salto)
cadena_sin_salto = cadena_con_salto.rstrip("\n").replace('con','sin')
print(cadena_sin_salto)
print("FIN\n")

#MEtodo insertar datos en una lista en una posicion especifica
print("Insertar en la posicion 4 especificamente de una lista un nuevo elemento")
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
print(frutas)
print()

#el método isdisjoint() para verificar si dos conjuntos no tienen elementos en común. Aquí tienes el código para verificar si los conjuntos marcas_smartphones y marcas_tv son conjuntos aislados
print("Método isdisjoint() para verificar si dos conjuntos no tienen elementos en común")
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)
print()