import re                    #  Expresiones Regulares
import os                    #  Trabajar con archivos
import time                  #  Duraccion del programa
import datetime              #  Fecha de hoy
from pathlib import Path     #  Trabajar con rutas
import math                  #  Trabajar con expresiones matematicas, redondeo de numéros

inicio = time.time()

ruta = 'E:\\Proyectos_Python\\Documentacion\\6.Modulos_Python\\Proyecto+Dia+9\\Mi_Gran_Directorio'

#\D{3} 3 caracteres que no sean números
#\d 5 datos numéricos
mi_patron = r'N\D{3}-\d{5}'

#Fecha actual
hoy = datetime.date.today()
#Listado de números encontrados vacia en el momneto
nros_encontrados = []
#Archivos encontrados que tengan el patron indicado
archivos_encontrados = []

#Funcion que busca en los archivos si se encuentra el patron indicado
def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

#Funcion que crea la lista con archivos que contengan el patron y los numeros de serie encotnrados
def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            #buscar_numero(Path(carpeta,a), mi_patron) crea una ruta con el nombre de la carpeta + el nombre del archivo
            resultado = buscar_numero(Path(carpeta,a), mi_patron)
            if resultado != '':
                #print(resultado.group()+" - "+a.title())
                #print(f"{carpeta} - {subcarpeta} - {a}")
                #print(carpeta.title().split('\\')[-1])
                nros_encontrados.append((resultado.group()))  # Grupo de resultados que retorna la coincidencia encontrada
                archivos_encontrados.append(a.title())        # Nombre del archivo que contiene el resultado encontrado

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Números encotrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)

crear_listas()
mostrar_todo()


