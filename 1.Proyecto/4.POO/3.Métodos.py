'''Los objetos creados a partir de clases también contienen métodos. Dicho de otra manera, los métodos son funciones que pertenecen al objeto.

Cada vez que un atributo del objeto sea invocado (por ejemplo, en una función), debe incluirse
self, que refiere a la instancia en cuestión, indicando la pertenencia de este atributo.

__init__ es un método especial utilizado como constructor de una instancia de una clase
'''

class Persona:
    especie = "humano"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}')

    def cumplir_anios(self, estado_humor):
        print(f'Cumplir {self.edad + 1} años me pone {estado_humor}')

    def tipo_objeto(self):
        print(f"{self.nombre.upper()} es del tipo de especie: '{self.especie}' y tiene {self.edad} años.")

juan = Persona("Juan", 37)
juan.saludar()
juan.cumplir_anios("feliz")
juan.tipo_objeto()

