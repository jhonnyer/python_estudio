'''
Las clases "hijas" que heredan de las clases superiores, pueden crear nuevos métodos o sobrescribir los de la clase "padre".
Asimismo, una clase "hija" puede heredar de una o más clases, y a su vez transmitir herencia a clases "nietas".

Si varias superclases tienen los mismos atributos o métodos, la subclase sólo podrá
heredar de una de ellas. En estos casos Python dará prioridad a la clase que se
encuentre más a la izquierda.

Del mismo modo, si un mismo método se hereda por parte de la clase "padre", e "hija",
la clase "nieta" tendrá preferencia por aquella más próxima ascendente
(siguiendo nuestro esquema, la tomará de la clase "hija").

un método dado se buscará primero en la propia clase, y de no hallarse, se explorará las superiores

Clase.__mro__ => devuelve el orden de resolución de métodos

super().__init__(arg1, arg2,...) => hereda atributos de las superclases de manera compacta
'''
print("\nEjemplo herencia extendida:\n")

class Animal:
    def __init__(self, edad, color):
        self.edad=edad
        self.color=color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        #self.edad=edad
        #self.color=color
        #Puedo heredar la construcción de los atributos de instancia con super()
        super().__init__(edad,color)
        self.altura_vuelo=altura_vuelo
    def hablar(self):
        print("pio")

    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")

class Perro(Animal):
    pass

print(''''\nEjemplo de herencia de la clase Pajaro a la clase Animal, en este caso hereda el método nacer() y hablar().
No obstante, el método hablar() es sobrescrito en la clase Pajaro, por lo cual la instancia creada de Pajaro da prioridad a esté método sobrescrito.\n''')
print("Para crear la instancia de Pajaro, en este caso se requiere 3 parametros (edad, color, altura_vuelo), mientras que en la herencia se requieren 2.")
piolin=Pajaro(2,'amarrillo', 60)
piolin.nacer()
piolin.hablar()

print("\nUtilización del método volar que pertenece a la clase hija Pajaro y no hereda de la clase Animal: ")
piolin.volar(100)

print("\nInstanciación de un objeto de la clase Animal, en este caso se requiere 2 parametros (edad, color) y no tiene los métodos de la clase Pajaro")
animal=Animal(2,'negro')
animal.hablar()

#################################################################################
######################    HERENCIA MULTIPLE   ###################################
#################################################################################

print()
print("*"*50)
print("Ejemplo herencia multiple:")
print("*"*50)
print()
class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja ja ja")

    def hablar(self):
        print("Soy un saludo de la madre")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

print("\nEjemplo heredación herencia multiple, clase Nieto hereda de Hijo, y clase Hijo hereda de la clase Padre y Madre, por lo tanto las instancias de la clase Nieto podran utilizar los métodos de la clase Hijo, y a su vez de Madre y Padre como reir() y hablar().")
print("En los casos de herencia multiple, si las clases heredadas tienen el mismo método como por ejemplo hablar(), la clase que hereda tiene en cuenta por jerarquia la clase que esta a la izquierda, en este caso la clase Padre  => class Hijo(Padre, Madre):")
mi_nieto=Nieto()
mi_nieto.hablar()
mi_nieto.reir()

print("\nVerificar el orden de procesamiento o resolución de los métodos heredados mediante la utilzación del método especial '__mro__' ")
print(Nieto.__mro__)


#########################################################
print("\nEjemplo de Herencia:")
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    def __init__(self):
        super().__init__()
        self.tiene_pico = True

    def amamantar(self):
        print("Amamantando crías")

# Crear un ornitorrinco
mi_ornitorrinco = Ornitorrinco()
print("¿Es un vertebrado?", mi_ornitorrinco.vertebrado)
print("¿Tiene pico?", mi_ornitorrinco.tiene_pico)
print("¿Es venenoso?", mi_ornitorrinco.venenoso)

mi_ornitorrinco.poner_huevos()
mi_ornitorrinco.nadar()
mi_ornitorrinco.caminar()
mi_ornitorrinco.amamantar()
print()

#############################################################
print("Ejemplo de herencia: \n")

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"



mi_hijo=Hijo()
print(mi_hijo.reir())
print(mi_hijo.hobby())
