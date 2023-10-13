'''La clase Path permite representar rutas de archivos en el sistema de archivos de nuestro sistema operativo. Se destaca por su legibilidad frente a alternativas semejantes.
Permite:
 * Crear o mover archivos
 * Enumerar archivos
 * Crear rutas basadas en Strings

base = Path.home() => Devuelve un objeto Path representando el directorio base del usuario
ruta = Path(base, "Europa" , "Barcelona" , "SagradaFamilia.txt") => Crear el archivo SagradaFamilia.txt con todas las carpetas anteriores como jerarquia de carpetas
    * base = Se aceptan strings y otros objetos Path

ruta2 = ruta.with_name("LaPedrera.txt")  => Devuelve un nuevo objeto Path cambiando únicamente el nombre de archivo

Cada invocación de la propiedad parent devuelve la ruta de jerarquía inmediata superior
'''

from pathlib import Path

print("Crear rutas a partir del método Path")
guia=Path("Barcelona",'Sagrada_Familiar')
print(guia)

guia=Path("Barcelona","lecturas",'Sagrada_Familiar.txt')
print(guia)

print("\nObtener una ruta base absoluta del directorio principal con el método Path.home():")
base=Path.home()
print(base)

print("\nConcatenar la ruta base con un directorio especifico creando una ruta absoluta con el nombre de un archivo txt:")
ruta=Path(base, "Barcelona",'Sagrada_familia.txt')
print(ruta)


print("\nGestión de dos rutas absolutas dentro de una ruta absoluta ya creada:")
ruta1=Path(base,"Europa", "España", Path("Barcelona",'Sagrada_familia.txt'))
print(ruta1)

print("\nCrear una nueva ruta de un archivo nuevo, a partir de la ruta especificada de un archivo existente:")
guia=Path(Path.home(),"España","Barcelona",'Sagrada_Familiar.txt')
guia2=guia.with_name("La_Pedrera.txt")
print(guia)
print(guia2)

print("\nParent es una instancia de PATH que retorna el antecedor inmediato de una ruta de archivos organizados en carpetas: ")
print("Cada vez que ejecutamos parent, nos retorna la ruta anterior de una ruta antecesora anteriormente. Parent nos genera un arbol de carpetas.\n")
print(guia2.parent)
print(guia2.parent.parent)
print(guia2.parent.parent.parent)
print()

###############################################
print("Encontrar los archivos txt que se encuentran dentro de un directorio utilizando un for  y el método glob('*.txt')")
ruta2=Path(Path.home(),"Europa")
for txt in Path(ruta2).glob("*.txt"):
    print(txt)


###############################################
print("\nEncontrar los archivos txt que se encuentran dentro de un directorio y subdirectorios utilizando un for  y el método glob('**/*.txt')")
ruta2=Path(Path.home(),"Europa")
for txt in Path(ruta2).glob("**/*.txt"):
    print(txt)


###############################################
print("\nEncontrar  rutas relativas relacionadas entre si")
ruta3=Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa=ruta3.relative_to(Path("Europa"))
en_espania=ruta3.relative_to(Path("Europa","España"))
en_europa=ruta3.relative_to(Path("Europa"))
print(en_europa)
print(en_espania)