#INSTALAR PAQUETES => Recursos extras creados por otros desarrolladores o comunidades de desarrollo
'''
Una de las grandes ventajas de Python como lenguaje de programación, es que cuenta con un amplia comunidad activa,
que desarrolla paquetes que añaden muchas más funcionalidades.

Si ya conoces el nombre del módulo que quieres instalar, puedes obtenerlo de PyPi directamente desde la consola:
            'pip install <modulo>'

PyPi (Python Package Index) es el repositorio de referencia para hallar paquetes desarrollados por la comunidad

También se puede actualizar los módulos que ya tengas instalados añadiendo --upgrade luego del nombre del paquete:
            'pip install <modulo> --upgrade'
'''

from colored import fg, bg, attr


print("Buscar paquete de Python en Google para instalar paquete para modificar color de texto de la consola, ejemplo: 'python packages for console text colors'")
print("Instalar paquete para modificar color de texto de la consola: 'pip install colored' en el terminal de mi host.")

print("\nPara utilizarlo debemos importarlo y aplicarselo al texto que queremos: \n")
print("from colored import fg, bg, attr")
print("color = fg(1) + bg(15)")  #fg(1) el color del texto rojo, bg(15) color de fondo blanco
print("print(color + 'Hola Mundo' + attr(0)") #attr(0) resetea para que no se siga aplicando a otros textos
print()

color = fg(1) + bg(15)
color + 'Hola Mundo' + attr(0)
print(color + 'Hola Mundo' + attr(0))

print("\nLibreria openpxyl para manejar archivos de excel: \n")
print("pip install openpyxl")
print("from openpyxl import *")
print()

print("Los paquetes se pueden instalar en PyCharm desde el instalador de paquetes")