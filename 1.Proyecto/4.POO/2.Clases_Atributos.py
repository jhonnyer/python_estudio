'''
Los atributos son variables que pertenecen a la clase. Existen atributos de clase (compartidos por todas las instancias de la
clase), y de instancia (que son distintos en cada instancia de la clase).

Cada objeto creado a partir de la clase puede compartir determinadas características:
atributos de clase => (por ejemplo: cantidad de caras)

Cada objeto creado a partir de la clase puede contener características específicas
atributos de instancia => (por ejemplo: color, altura, ancho, largo...)

Todas las clases tienen una función que se ejecuta al instanciarla, llamada __init__(), y
que se utiliza para asignar valores a las propiedades del objeto que está siendo creado.
self: representa a la instancia del objeto que se va a crear

los parámetros de la función __init__ se entregan a los atributos de instancia
'''

#Los atributos se instancia, cada objeto puede tener un parametro distinto
print("Atributos de instancia: \n")

class Pajaro:
    #Método constructor de la clase Pajaro, cada que llamamos una clase, python llama a su método constructor de la clase e inicializa los atributos de instancia
    def __init__(self, color, especie):
        self.color=color  # self.color es el atributo, y color es el párametro, el valor que le asignamos en la creación de la instancia
        self.especie=especie

mi_pajaro=Pajaro('azul','Tulcan')
print(mi_pajaro)
#Acceder al valor del atributo color de la clase pajaro
print("Verificar atributo color y especie de la clase pajaro: ")
print(mi_pajaro.color)
print(mi_pajaro.especie)
print()

###################################################################
print("Atributos de clase, los cuales son iguales para todos los objetos que se vayan a crear de una clase: \n")
class Pajaro:
    alas=True #Todos los pajaros van a tener alas, no es necesario enviar el parametro en la instancia del objeto
    #Método constructor de la clase Pajaro, cada que llamamos una clase, python llama a su método constructor de la clase e inicializa los atributos de instancia
    def __init__(self, color, especie):
        self.color=color  # self.color es el atributo, y color es el párametro, el valor que le asignamos en la creación de la instancia
        self.especie=especie

mi_pajaro=Pajaro('azul','Tulcan')
print("Verificar atributo alas (instancia de clase), color y especie de la clase pajaro: ")
print(f"Mi pajaro es un: {mi_pajaro.especie} y es de color {mi_pajaro.color}")
print("Verificacion si tiene alas")
print(mi_pajaro.alas)
print()

##################
print("Ejemplo clase Personaje:")


class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje("Humano", True, "17")
print(harry_potter)