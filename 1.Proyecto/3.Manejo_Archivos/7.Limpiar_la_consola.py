'''
Para controlar la información mostrada al usuario en consola podemos limpiarla, eliminando los diferentes mensajes que han aparecido conforme se va ejecutando el programa.

from os import system

En Unix/Linux/MacOS  => system("clear")
En DOS/Windows:  => system("cls")
'''

from os import system

nombre=input("Dime tu nombre: ")
edad=input("Dime tu edad: ")
#para windows cls para linux clear
system('cls')
print(f"Tu nombre es: {nombre} y tienes {edad} años")