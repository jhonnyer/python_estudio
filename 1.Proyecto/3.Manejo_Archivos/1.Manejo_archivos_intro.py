'''La manipulación de archivos desde Python se engloba bajo las funciones de E/S (entrada/salida)
 o I/O (en inglés: input/output). Comenzaremos explorando las funciones utilizadas para abrir, leer y cerrar archivos '''

'''
* open(archivo, modo): abre un archivo, y devuelve un objeto de tipo archivo
sobre el que pueden aplicarse métodos

* readline(bytes): devuelve una línea del archivo, limitada por el número
indicado en el parámetro tamaño (en bytes).

* read(bytes): devuelve un número especificado de bytes del archivo. De manera predeterminada 
(sin indicar un valor en el argumento bytes), devolverá el archivo completo (equivalente a escribir -1).

* readlines(bytes): devuelve una lista que contiene cada una de las líneas del archivo como item 
de dicha lista. Si el tamaño excede lo indicado en el parámetro bytes, no se devolverán líneas 
adicionales. 

* close( ): cierra el archivo abierto, tal que no puede ser leído o escrito
luego de cerrado. Es una buena práctica utilizar este método si ya no
será necesario realizar acciones sobre un archivo.'''

print("Metodo open() para abrir archivos\n")
ruta_archivo = r'E:\Proyectos_Python\Documentacion\3.Manejo_archivos\Prueba.txt'
mi_archivo=open(ruta_archivo)
#print(mi_archivo.read())
#print()

#print("Leer la primer linea del archivo")
#primer_linea=mi_archivo.readline()
#print(primer_linea)
#primer_linea=mi_archivo.readline()
#print(primer_linea)
#primer_linea=mi_archivo.readline()
#print(primer_linea)

print("Leer la primer linea y eliminar el salto de linea ultimo")
primer_linea=mi_archivo.readline().rstrip()
print(primer_linea)

print("\nPython cada vez que utiliza el readline() o read() guarda un punto desde la ultima vez, y continua en el siguiente punto como reservando un espacio de memoria\n")
print("Todos los métodos de string son aplicables a estos textos, en este caso convertir a mayuscula")
print(primer_linea.upper())
mi_archivo.close()

#################################################################
print("\nRecorrer las líneas de un archivo con for\n")
ruta_archivo = r'E:\Proyectos_Python\Documentacion\3.Manejo_archivos\Prueba.txt'
mi_archivo=open(ruta_archivo)
contador=1
for l in mi_archivo:
    print(f'La linea {contador} tiene el siguiente texto: {l.rstrip()}')
    contador+=1
mi_archivo.close()

#################################################################
print("\nCrear una lista a partir de las lineas de un archivo de texto, con metodo readlines() en plural")
ruta_archivo = r'E:\Proyectos_Python\Documentacion\3.Manejo_archivos\Prueba.txt'
mi_archivo=open(ruta_archivo)
lista_lineas=mi_archivo.readlines()
print(lista_lineas[0])
print(lista_lineas)
print("Remover una linea de la lista con método pop()")
remover=lista_lineas.pop()
print(remover)

print("Remover una linea especifica de la lista con método pop(0)")
remover=lista_lineas.pop(0)
print(remover)
mi_archivo.close()

print("\nMetodo open() para abrir archivos dentro de un try catch\n")
ruta_archivo = r'E:\Proyectos_Python\Documentacion\3.Manejo_archivos\Prueba.txt'
try:
    with open(ruta_archivo, 'r') as mi_archivo:
        # Realiza operaciones con el archivo aquí
        contenido = mi_archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró en la ruta especificada.")