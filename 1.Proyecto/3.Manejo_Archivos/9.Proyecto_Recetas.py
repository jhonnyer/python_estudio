import os
from  pathlib import  Path
from  os import  system
import time

#Configuracion rutas
mi_ruta=Path(Path.home(),'Recetas')

#Funcion para contar recetas
def contar_recetas(ruta):
    contador=0
    for txt in Path(ruta).glob("**/*.txt"):
        contador +=1
    return contador

#Funcion menu principal
def menu_inicio():
    eleccion_menu='x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opción: ")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa  
        ''')
        print()
        eleccion_menu=input()
    return eleccion_menu

#Funcion de inicio
def inicio():
    system('cls')
    print()
    print("*"* 50)
    print("*"* 5+"Bienvenido al administrador de recetas "+"*"*5)
    print("*"* 50)
    print(f"\nLas recetas se encuentran en: {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")
    opcion=menu_inicio()
    return opcion


#Funcion para mostrar la categoria de las recetas
def mostrar_categorias(ruta):
    print("\nCategorias: ")
    ruta_categorias =Path(ruta)
    lista_categorias = []
    contador= 1
    #iterdir es un método que permite iterar en cada directorio y obtener otros directorios que esten en este
    #En este caso, estamos iterando sobre el directorio Recetas y recuperamos el nombre de los directorios existentes dentro de Recetas
    for carpeta  in ruta_categorias.iterdir():
        carpeta_str=str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador +=1
    return lista_categorias

#Funcion para elegir la categoria de las recetas a verificar
def elegir_categoria(lista):
    eleccion_correcta='x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista)+1):
        eleccion_correcta=input("\nElige una categoría: ")
    return lista[int(eleccion_correcta) - 1]

#Funcion para mostrar las recetas existentes en la categoria
def mostrar_recetas(ruta):
    print("\nRecetas: ")
    ruta_recetas=Path(ruta)
    lista_recetas=[]
    contador=1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str=str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador +=1
    return lista_recetas

#Funcion para elegir la receta a verificar
def elegir_receta(lista):
    eleccion_receta='x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista)+1):
        eleccion_receta=input("\nElige una receta: ")
    return lista[int(eleccion_receta)-1]

#Funcion leer receta
def leer_receta(receta):
    print(Path.read_text(receta))

#Funcion crear receta
def crear_receta(ruta):
    existe=False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta=input()+'.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta=input()
        ruta_nueva=Path(ruta, nombre_receta)
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe=True
        else:
            print("Lo siento, esa receta ya existe")

#Funcion crear categoría
def crear_categoria(ruta):
    existe=False
    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nueva_categoria=input()
        ruta_nueva=Path(ruta, nueva_categoria)
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nueva_categoria} ha sido creada\n")
            time.sleep(1)
            existe=True
        else:
            print("Lo siento, esa categoria ya existe\n")

#Funcion eliminar receta
def eliminar_receta(receta):
    Path(receta).unlink() #unlink es un método utilizado para eliminar archivos
    print(f"La receta {receta.name} ha sido eliminada\n")
    time.sleep(1)

#Funcion eliminar categoria
def eliminar_categoria(categoria):
    Path(categoria).rmdir() #rmdir es un método utilizado para eliminar directorios o carpetas
    print(f"La categoria {categoria.name} ha sido eliminada\n")
    time.sleep(1)

#Funcion volver al inicio():
def volver_al_inicio():
    eleccion_regresar='x'
    while eleccion_regresar.lower()!='v':
        eleccion_regresar=input("\nPresione V para volver al menú: ")


finalizar_programa = False
while not finalizar_programa:
    menu=inicio()
    match menu:
        case "1":
            mis_categorias=mostrar_categorias(mi_ruta)
            mi_categoria=elegir_categoria(mis_categorias)
            mis_recetas= mostrar_recetas(mi_categoria)
            if len(mis_recetas) < 1:
                print("No hay recetas en esta categoría.\n")
            else:
                mi_receta=elegir_receta(mis_recetas)
                leer_receta(mi_receta)
            volver_al_inicio()
        case "2":
            mis_categorias=mostrar_categorias(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            crear_receta(mi_categoria)
            volver_al_inicio
        case "3":
            crear_categoria(mi_ruta)
            volver_al_inicio
        case "4":
            mis_categorias=mostrar_categorias(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            mis_recetas = mostrar_recetas(mi_categoria)
            if len(mis_recetas) < 1:
                print("no hay recetas en esta categoría.")
            else:
                mi_receta=elegir_receta(mis_recetas)
                eliminar_receta(mi_receta)
            volver_al_inicio
        case "5":
            mis_categorias=mostrar_categorias(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            eliminar_categoria(mi_categoria)
            volver_al_inicio
        case "6":
            finalizar_programa=True
