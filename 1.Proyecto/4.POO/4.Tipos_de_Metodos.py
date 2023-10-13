'''
Los métodos estáticos y de clase anteponen un decorador específico, que indica a Python el
tipo de método que se estará definiendo

Así como los métodos de instancia requieren del parámetro self para acceder a dicha instancia, los métodos de clase requieren del parámetro cls para acceder a los atributos de clase. Los métodos estáticos, dado que no pueden acceder a la instancia ni a la clase, no indican un parámetro semejante.

Decoradores:
    * Métodos de instancia => Reciben parametro self cuando se definen.
        - Pueden accerder y modificar atributos del objeto
        - Pueden acceder a otros métodos
        - Modificar el estado de la clase
    * Métodos de clase  => @classmethod
        - Reciben el parametro cls de clase, estan asociados a la clase en sí misma.
        - Pueden ser llamados desde una instancia de la clase, como tambien desde la clase misma.
    * Métodos de instancia => @staticmethod
        - No aceptan como parametro ni self, ni cls, por lo cual no pueden modificar el estado de una instancia
        - Pueden aceptar paramtros de entrada
        - Funciones normales ligados a una clase
'''

print("Ejemplo método de instancia\n")
class Pajaro:
    alas=True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuelva {metros} metros")
        self.piar() #los métodos de instancia peuden ser llamados desde otros métodos

    def pintar_negro(self):
        self.color='negro'
        print(f"Ahora el pajaro es {self.color}")

    #Creación de un método de clase
    @classmethod
    def poner_huevos(clsc, cantidad):
        print(f"Puso {cantidad} huevos")
        #Puedo modificar los atributos de clase
        clsc.alas=False
        print(f"Pajaro tiene el atributo alas en: {Pajaro.alas}")
        # Los métodos de clase solo ejecutan atributos de clase, no es posible acceder a los atributos de instancia
        #print(f"Es de color {self.color}")

    #Método estático => Sirven para asegurar métodos que no se quiere que modifique el estado de las instancias y sus atributos
    #Los métodos estaticos pueden ser llamados por el nombre de la clase o una instancia
    @staticmethod
    def mirar():
        print("El pajaro tiene unas alas grandes")
        #Los métodos estáticos no pueden aceder ni a los atributos de clase ni a los atributos de instancia
        #self.colo='rojo'
        #cls.alas =False

##########################################################################
############# Ejecutar diferentes métodos de clase #######################
##########################################################################

piolin= Pajaro('amarillo','canario')
piolin.pintar_negro()
piolin.volar(4)
print("Modificar los estados de la clase mediante un método de la instancia, en este modificamos el valor de alas")
piolin.alas=False
print(piolin.alas)

#Los métodos de clase pueden ser ejecutados directamente sin necesitar una instancia creada anteriormente
#Los métodos de clase solo ejecutan atributos de clase, no es posible acceder a los atributos de instancia
print("Ejemplo método de clase, el cual puede ser invocado directamente desde la clase Pajaro o desde una instancia: \n")
Pajaro.poner_huevos(3)
piolin.poner_huevos(12)
print()

#Los métodos estaticos pueden ser llamados por una clase o por una instancia
print("Ejemplo método estático, el cual puede ser invocado directamente desde la clase Pajaro o desde una instancia: \n")
Pajaro.mirar()
piolin.mirar()
print()

###############################
#Ejemplo método de instancia
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
        print(f"Ahora tiene {self.cantidad_flechas} flechas")

persona=Personaje(10)
persona.lanzar_flecha()