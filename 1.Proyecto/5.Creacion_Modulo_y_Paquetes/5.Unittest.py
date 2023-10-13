'''
Unit Testing es un método o herramienta utilizado en programación para determinar si un módulo o un conjunto de módulos de código
funciona correctamente. Dicha evaluación se realiza en un archivo independiente. En Python, se implementa desde el módulo incorporado unittest.
import unittest
import mimodulo

class NombrePrueba(unittest.TestCase):
def test_prueba(self):
    primer_valor = {algo}
    segundo_valor = {salida de mimodulo.funcion}
    self.assertEqual(primer_valor, segundo_valor, mensaje)

Los primeros dos argumentos de assertEqual son dos valores que se comparan para establecer si hay igualdad entre
ellos. Por eso, uno debe obtenerse a partir de una función del módulo evaluado, y otro ser la salida esperada para una
misma entrada de información que en el primer caso. El tercer parámetro (mensaje), contendrá un string con información
que se mostrará al usuario en caso de que el test falle.

Antes incluso de ejecutar el código, Python lee el archivo para definir algunas variables globales. Una de ellas es
__name__, que toma el nombre "__main__" en caso que Python esté corriendo en dicho módulo de manera
individual. Si por el contrario, el módulo fuera importado, la variable __name__ toma el nombre del módulo. Este bloque
de código evalúa que la prueba se esté ejecutando directamente.
'''

import unittest
import cambia_texto_unnitest

#La clase ProbarCambiaTexto Hereda los métodos de test de Unnitest
class ProbarCambiaTexto(unittest.TestCase):
    #El nombre del metodo de testeo debe empezar con la palabra test
    def test_mayusculas(self):
        palabra='buen dia'
        resultado=cambia_texto_unnitest.todo_mayusculas(palabra)
        #Verificamos si el resultado de utilizar el metodo todo_mayuscula es igual en este caso a 'BUEN DIA'
        self.assertEquals(resultado,'BUEN DIA')

    def test_mayusculas_error(self):
        palabra='buen dia'
        resultado=cambia_texto_unnitest.todo_mayusculas(palabra)
        #Verificamos si el resultado de utilizar el metodo todo_mayuscula es igual en este caso a 'BUEN DIA'
        self.assertEquals(resultado,'buen dia')

    #Verifica que la primer letra de cada palabra sea mayuscula
    def test_primer_letra_mayuscula(self):
        palabra='buen dia'
        resultado=cambia_texto_unnitest.primer_letra_mayuscula(palabra)
        #Verificamos si el resultado de utilizar el metodo todo_mayuscula es igual en este caso a 'BUEN DIA'
        self.assertEquals(resultado,'Buen Dia')

#Forma de decirle al sistema en Python cual es la función principall
if __name__=='__main__':
    unittest.main()

