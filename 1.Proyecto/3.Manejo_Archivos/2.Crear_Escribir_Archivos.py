'''
El método Open para tratar archivos recibe dos parametros, el primero el nombre del archivo a abrir,
el segundo la propiedad que indica los permisos de lectura, escritura del archivos.
Ejemplo: mi_archivo = open('archivo.txt', 'r')

Propiedades:

r= Permiso de solo lectura
w= Permiso de solo escritura, si el archivo ya existe se vacea el contenido y se escribe uno nuevo. Si no existe el archivo se crea uno nuevo
a= Permiso de solo escritura al final del archivo, si el archivo no existe se crea y si existe se escribe el contenido al final
'''


#################################################################
print("\nPermiso de solo lectura 'r'\n")
ruta_archivo = r'E:\Proyectos_Python\Documentacion\3.Manejo_archivos\Prueba.txt'
mi_archivo=open(ruta_archivo,'r')
print(mi_archivo.read())
#mi_archivo.write('Soy un texto nuevo')  #No se puede escribir texto en un archivo que ha sido abierto con permiso de solo lectura ('r')
mi_archivo.close()


#################################################################
print("\nPermiso de solo escritura 'w'\n")
ruta_archivo1 = r'E:\Proyectos_Python\Documentacion\3.Manejo_archivos\Prueba_solo_escritura.txt'
mi_archivo_escritura=open(ruta_archivo1,'w')
#Manejo de salto de linea con \n o '''Texto con espacios '''
mi_archivo_escritura.write('Soy un texto nuevo\n')
mi_archivo_escritura.write('Bienvenido al curso de python\nEstamos probando escritura sobre un archivo.\n\n')
mi_archivo_escritura.write('''Hemos visto:

*Tipos de datos
*Métodos de los objetos
*Funciones
*Procesamiento de archivos
''')
#Otra forma de escribir en un archivo, aunque es confuso, escribe un string uno despues del otro, no es recomendable utilizarlo
mi_archivo_escritura.writelines(['Vamos, ','a empezar ',' el curso de Python\n','Comenzemos\n\n' ])
#Se puede utilizar una lista y darle espacios de la siguiente forma:
lista=['Escritura','de','texto','con','writelines','utilizando','recorrido','de','lista en un for','y saltando espacios\n\n']
for p in lista:
    mi_archivo_escritura.writelines(p+'\n')

lista1=['Escritura','de','texto','con','writelines','utilizando','recorrido','de','lista en un for','en una sola linea,','añadiendo espacio entre palabras de la lista.']
for p in lista1:
    mi_archivo_escritura.writelines(p+' ')
mi_archivo_escritura.close()


mi_archivo_escritura=open(ruta_archivo1)
print(mi_archivo_escritura.read())
mi_archivo_escritura.close()
print("FIN SOLO ESCRITURA CON 'W'")

#################################################################
print("\nPermiso de solo escritura al final del archivo 'a', sin eliminar contenido anterior, es decir sobreescribir un archivo\n")
mi_archivo_a=open(ruta_archivo1,'a')
mi_archivo_a.write("\n\nSoy un texto nuevo añadido al final del texto con permiso de solo escritura al final 'a'\n")
mi_archivo_a.close()

mi_archivo_a=open(ruta_archivo1,'r')
resultado=mi_archivo_a.read()
mi_archivo_a.close()
print(resultado)

############################
print("EJEMPLO RECORRER LISTA Y ESCRIBIR EN UN ARCHIVO NUEVO UTILIZANDO TABULADOR PARA SEPARAR TEXTO")
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
ruta = r'E:\Proyectos_Python\Documentacion\3.Manejo_archivos\registro.txt'
archivo = open(ruta, 'a')
for i in registro_ultima_sesion:
    archivo.write(i+'\t')
archivo.close()

archivo = open(ruta, 'r')
resultado = archivo.read()
archivo.close()
print(resultado)

