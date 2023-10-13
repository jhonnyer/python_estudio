'''
El módulo Shutil ofrece funcionalidades de alto nivel sobre archivos, tales como copiar, crear, eliminar y mover entre
directorios. También mencionaremos métodos del módulo os que cumplen objetivos similares.

import shutil

* shutil.move(archivo, directorio) : mueve un archivo desde el directorio actual hacia aquel que se especifica en el segundo parámetro.
* os.unlink(directorio) : elimina un archivo del directorio indicado
* os.rmdir(directorio) : elimina una carpeta vacía
* shutil.rmtree(directorio) : elimina una carpeta indicada en el directorio, incluyendo todas sus ramificaciones (subcarpetas y archivos), de manera definitiva y sin pasar porla papelera de reciclaje.
* send2trash.send2trash(archivo) : envía un archivo a la papelera de reciclaje (es necesario instalar el módulo 'pip install Send2Trash' desde y luego importarlo)
* os.walk(directorio) : recorre el directorio indicado, y devuelve los nombres de carpetas, subcarpetas y archivos dentro de ellas en forma de tupla, a través de un generador
'''

import os
import shutil
import send2trash

print("Ruta donde me encuentro con os.getcwd()")
print(os.getcwd())

print("Creo un archivo nuevo")
archivo = open('curso.txt','w')
archivo.write('texto_prueba')
archivo.close()
print("Imprime en una lista todos los archivos que estan en el directorio actual")
print(os.listdir())

print("Mover archivo utilizando shutil")
shutil.move('curso.txt','E:\\Proyectos_Python\\Documentacion\\6.Modulos_Python')

print("Eliminar la carpeta y archivos en una ruta especifica, tener cuidado el metodo rmtree(). Este método no almacena en la papelera ojo porque no se puede restaurar. :")
shutil.rmtree('E:\\Proyectos_Python\\Documentacion\\6.Modulos_Python\\prueba')

print("Para almacenar los archivos eliminados en papelera podemos utilizar: 'import send2trash' ")
send2trash.send2trash('E:\\Proyectos_Python\\Documentacion\\6.Modulos_Python\\curso.txt')


print("Verificar estructura directorios y archivos con el método os.walk() que es un generador que va entregando informacion a medida que es pedida, no ocupa espacio de memoeria. Crea tuplas con la informacion de la carpeta, subcarpeta y archivos encontrados.")
ruta='E:\\Proyectos_Python\\Documentacion'
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print('Los archivos son: ')
    for arc in archivo:
        #print(f"\n{arc}")
        #Filtrar por el nombre de un archivo, en este caso que empiece por 2023
        if arc.startswith('2023'):
            print(f"\t{arc}")
    print("\n")