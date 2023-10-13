'''
Pylint es un verificador de código, errores y calidad para Python, siguiendo el estilo recomendado por PEP 8, la guía de estilo de Python. Es de gran utilidad en el trabajo en equipo
             'pip install pylint'
Ejecutar desde la consola:   => pylint modulo1.py -r y

Al ejecutarse, Pylint devuelve un reporte con las características que fueron evaluadas, errores y puntuaciones parciales
A mayor puntaje, mayor será la calidad de tu código. Un umbral aceptable será >= 7.00/10

#Unnitest => Probar los programas y verificar los resultados deseados

#Verificar instalacion: => pip show pylint

POR CONVENCION  SE EXIGE:
    * El módulo debe tener un comentario inicial que indique que hace el código
    * El código debe ser implementado en una funcion.
'''
numero1= 500
#print(Numero1)  #Código mal
#print(numero1)  #Código Bien
print("Verificar errores con pylint => pylint nombre_archivo.py -r y")

print('''\n
POR CONVENCION  SE EXIGE => recomendaciones de estilo PEP 8:
    * El módulo debe tener un comentario inicial que indique que hace el código
    * El código debe ser implementado en una funcion.
''')
