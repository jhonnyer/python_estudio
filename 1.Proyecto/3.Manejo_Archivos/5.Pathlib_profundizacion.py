'''
El módulo pathlib, disponible desde Python 3.4, permite crear objetos Path, generando rutas que pueden ser interpretadas por diferentes sistemas operativos y cuentan con una serie de propiedades útiles.

from pathlib import Path
ruta = Path("C:/Users/Usuario/Desktop")

A partir de una semántica sencilla, devuelve una ruta que el sistema puede comprender. Por ejemplo, en Windows, devolverá:''' #C:\Users\Usuario\Desktop y en Mac: C:/Users/Usuario/Desktop
'''Navegación:
ruta = Path("C:/Users/Usuario/Desktop") / "archivo.txt"

Es posible concatenar objetos Path y strings con el delimitador "/" para construir rutas completas. Permite manejar rutas de archivos de manera rapida y óptima
Algunos métodos y propiedades sobre objetos Path son:

* read_text( ): lee el contenido del archivo sin necesidad de abrirlo y cerrarlo
* name: devuelve el nombre y extensión del archivo
* suffix: devuelve la extensión del archivo (sufijo)
* stem: devuelve el nombre del archivo sin su extensión (sufijo)
* exists(): verifica si el directorio o archivo al que referencia el objeto Path existe y devuelve un booleano de acuerdo al resultado (True/False) '''

#PureWindowsPath nos permite importar la ruta de Windows pura, transformar cualquier ruta que tenga en una ruta de windows
from pathlib import Path, PureWindowsPath

print("Manejo de archivos utilizando objeto PATH, que es generico para cualquier sistema operativo. En este caso la ruta se escribe con el uso de barras invertidas '/'")
carpeta = Path('E:/Proyectos_Python/Documentacion/3.Manejo_archivos/alternativa/registro.txt')
print("\nLeer texto con el método read_text() del objeto PATHLIB, no es necesario ni abrir ni cerrar la conexión del archivo: ")
print(carpeta.read_text())

print("\nRetornar el nombre del archivo con el método name: ")
print(carpeta.name)
print("\nRetornar el sufijo o extensión del archivo con el método suffix: ")
print(carpeta.suffix)

print("\nRetornar el nombre del archivo sin la extensión con el método stem: ")
print(carpeta.stem)

#############################################
print("\nVerificar si un archivo existe con el metodo exists(), retorna un True o False ")
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, el archivo si existe")

#############################################
ruta_not_exist = Path('E:/Proyectos_Python/Documentacion/3.Manejo_archivos/alternativa/registros.txt')
print("\nVerificar que un archivo NO existe con el metodo exists(), retorna un True o False ")
if not ruta_not_exist.exists():
    print("Este archivo no existe")
else:
    print("Genial, el archivo si existe")

print()

#################################################
print("Convertir cualquier ruta, en una ruta pura de Windows con PureWindowsPath")
ruta_windows=PureWindowsPath(carpeta)
print(ruta_windows)

##########################
print("\nIndexación con parents: 'ruta.parents[0], ruta.parents[1], ruta.parents[2], ruta.parents[3]': ")
ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[0]
print(carpeta)

carpeta = ruta.parents[1]
print(carpeta)

carpeta = ruta.parents[2]
print(carpeta)

carpeta = ruta.parents[3]
print(carpeta)

'''
En la biblioteca pathlib de Python, puedes acceder a los directorios padres de una ruta utilizando la lista parents. Los índices en la lista parents se utilizan para especificar cuántos niveles de directorios hacia arriba deseas navegar desde la ruta actual. El índice 0 se refiere al directorio actual, el índice 1 se refiere al directorio padre (un nivel hacia arriba), el índice 2 se refiere al abuelo (dos niveles hacia arriba), y así sucesivamente.

En el código, se está usando ruta.parents[3], lo que significa que estás accediendo al cuarto directorio padre desde la ruta ruta. Aquí hay una ilustración de cómo funciona:

*Si usas ruta.parents[0], obtendrás: 
        C:/Users/Usuario/Desktop/Curso Python/Cuestionario Día 6/Pregunta 1

* Si usas ruta.parents[1], obtendrás:
        C:/Users/Usuario/Desktop/Curso Python/Cuestionario Día 6

y así sucesivamente
'''