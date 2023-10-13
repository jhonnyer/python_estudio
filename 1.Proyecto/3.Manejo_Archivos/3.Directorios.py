'''
Trabajar sobre archivos que se encuentran en directorios diferentes al de nuestro código requiere del soporte del módulo
OS, que contiene una serie de funciones para interactuar con el sistema operativo.

import os

* os.getcwd(): obtiene y devuelve el directorio de trabajo actual. Será el mismo en el que corre el programa si no se ha modificado.
* os.chdir(ruta): cambia el directorio de trabajo a la ruta especificada
* os.makedirs(ruta): crea una carpeta, así como todas las carpetas intermedias necesarias de acuerdo a la ruta especificada.
* os.path.basename(ruta): dada una ruta, obtiene el nombre del archivo (nombre de base)
* os.path.dirname(ruta): dada una ruta, obtiene el directorio (carpeta) que almacena el archivo
* os.path.split(ruta): devuelve una tupla que contiene dos elementos: el directorio, y el nombre de base del archivo.
* rmdir(ruta): elimina el directorio indicado en la ruta.

En Windows, es necesario indicar las rutas con dobles barras invertidas (\\) para que sean correctamente interpretadas por Python
'''
import  os;
print("Manejo de archivos mediante directorios\n")
print("Obtener la ruta del directorio actual mediante método os.getcwd()\n")
ruta =os.getcwd(); #Obtener directorio del trabajo actual
print(ruta)

###############################
print(r"Cambia directorio de trabajo con método os.chdir, importante doble '\\' para la ruta del archivo"+'\n')
ruta =os.chdir('E:\\Proyectos_Python\\Documentacion\\3.Manejo_archivos\\alternativa');
print(f"Abrir un archivo en una ubicación distinta, en este caso en: '{os.getcwd()}'")
archivo = open('registro.txt')
print(archivo.read())


###############################
print("\nCrear una carpeta nueva con método os.makedirs")
ruta =os.makedirs('E:\\Proyectos_Python\\Documentacion\\3.Manejo_archivos\\alternativa\\carpeta_nueva');


###############################
print("\nEliminar una carpeta con método os.rmdir")
ruta =os.rmdir('E:\\Proyectos_Python\\Documentacion\\3.Manejo_archivos\\alternativa\\carpeta_nueva');


###############################
print(r"Obtener la ruta 'os.path.direname(ruta)' y el nombre de un archivo con el método 'os.path.basename(ruta)'")
ruta ='E:\\Proyectos_Python\\Documentacion\\3.Manejo_archivos\\alternativa\\registro.txt';
elemento=os.path.basename(ruta)
ruta_elemento=os.path.dirname(ruta)
print(elemento)
print(ruta_elemento)


###############################
print("\n\nObtener la ruta y el nombre de un archivo como una tupla con el método 'os.path.split(ruta)'")
ruta ='E:\\Proyectos_Python\\Documentacion\\3.Manejo_archivos\\alternativa\\registro.txt';
elemento=os.path.split(ruta)
print(elemento)
ruta_elem, name_elemen=os.path.split(ruta)
print(ruta_elem + "  -  "+name_elemen)