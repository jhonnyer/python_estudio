'''
Una expresión regular es una secuencia de caracteres que forman un patrón de búsqueda determinado. Pueden ser
utilizadas para verificar strings en búsqueda de un contenido (patrón) específico. Utilizamos el módulo re en Python.

import re

Funciones:
* search( ): devuelve un objeto "match" que contiene información acerca del hallazgo si se encuentra en algún punto del string
* findall( ): devuelve una lista que contiene todos los hallazgos del patrón

Para formar patrones, utilizamos los siguientes cuantificadores y caracteres especiales:

[ ]   => un set de caracteres
.     => un carácter cualquiera
^     => inicia con
$     => finaliza con
*     => cero o más ocurrencias
+     => una o más ocurrencias
{ }   => un número especificado de ocurrencias
?     => cero o una ocurrencia
|     => operador lógico "O"

\d  => dígito numérico
\D  => NO numérico
\w  => caracter alfanumérico
\W  => NO alfanumérico
\s  => espacio en blanco
\S  => NO espacio en blanco

patron = r'\w{4}\d{4}'
verificar = re.search(patron,"cont1234")
'''
import re

print("Ejemplo RE 1, 4 caracteres alfanuméricos y 4 caracteres numéricos")
patron = r'\w{4}\d{4}'
verificar = re.search(patron,"cont1234")
print(verificar)
print()

print("Ejemplo RE patron '###-###-####', # signigica un dato númerico => patron = r'\d\d\d-\d\d\d-\d\d\d\d'")
patron = r'\d\d\d-\d\d\d-\d\d\d\d'   # Letra d significa digito
verificar = re.search(patron,"123-434-43434")
print(verificar)
print()

print("Ejemplo RE patron '###-###-####', # signigica un dato númerico => patron = r'\d{3}-\d{3}-\d{4}'")
print("Un número entre corchetes significa que un dato de re se va a repetir n veces")
patron = r'\d{3}-\d{3}-\d{4}'   # Letra d significa digito
verificar = re.search(patron,"123-434-43434")
print(verificar)
print()


print("Ejemplo RE patron 'V#.##', # signigica un dato númerico => patron = r'v\d.\d{2}'")
patron = r'v\d.\d{2}'   # Letra d significa digito
verificar = re.search(patron,"v1.02")
print(verificar)
print()



print("Ejemplo RE espacio en blanco \s => patron = r'número\s\d{2}'")
patron = r'número\s\d{2}'
verificar = re.search(patron,"número 23")
print(verificar)
print()


print("Ejemplo RE no númerico (cualquier combinación de letras => patron = r'\D'")
patron = r'\D{4}'
verificar = re.search(patron,"C-Ec")
print(verificar)
print()



print("Ejemplo RE no alfanumérico (cualquier combinación de signos => patron = r'\W'")
patron = r'\W{3}'
verificar = re.search(patron,"$#%!")
print(verificar)
print()

print("Ejemplo RE no espacios en blanco \S => patron = r'\S{4}'")
patron = r'\S{4}'
verificar = re.search(patron,"número 23")
print(verificar)
print()

print("Ejemplo cuantificadores para optimizar los filtros por expresiones regulares:")
print("Cuantificador + permite que aparezcan los valores definidos en la expresion las veces que sea necesario  =>  patron = r'código_\d-\d+'")
patron=r'código_\d-\d+'
verificar=re.search(patron,"prueba código_1-45")
print(verificar)
print()

print("Expresión {n,m} signigica que se va repetir de n a me veces, ejemplo:  =>  patron=r'\w{3,5}'   => (hola, sol, mundo, yo546, ...)")
patron=r'\w{3,5}'
verificar=re.search(patron,"hola")
print(verificar)
print()


print("Expresión {n,} signigica que se va repetir de n hasta arriba sin limite, ejemplo:  =>  patron=r'-\d{4,}-' ")
patron=r'-\d{4,}-'
verificar=re.search(patron,"-54652334234-")
print(verificar)
print()


print("Expresión *  signigica cero o más veces, ejemplo:  =>  patron=r'-\W\s*\W'    => (a 2, a    b, fm, s4) ")
patron=r'\w\s*\w'
verificar=re.search(patron,"a 2")
print(verificar)
verificar=re.search(patron,"a   b")
print(verificar)
verificar=re.search(patron,"fm")
print(verificar)
print()


print("Expresión ? significa que una palabra aparezca una vez o ninguna, permite validar palabras que no sabemos si van a aparecer en plural o singular.")
patron=r'casa?'
verificar=re.search(patron,"Hasta ayer tenia una casa")
print(verificar)
verificar=re.search(patron,"Hasta ayer tenia varias casas")
print(verificar)
print()

print("*"*50)
print("*"*15+" EJEMPLOS RE TEXTOS "+"*"*15)
print("*"*50)
print()

texto="Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"
print("Verificación sin utilizar RE")
palabra='ayuda' in texto
print(palabra)
print()
print("Verificación  utilizando RE mediante el metodo search. En este caso, este método solo encuentra la primer coincidencia.")
patron='ayuda'
busqueda=re.search(patron,texto)
print(busqueda)
print("Podemos verificar con span() la posición en la que se encuentra la palabra encontrada")
print(busqueda.span())
print("Podemos verificar con start() la posicion de inicio de la palabra encontrada")
print(busqueda.span())
print("Podemos verificar con end() la posicion de fin de la palabra encontrada")
print(busqueda.end())
print()


print("Verificación  utilizando RE mediante el metodo findall. En este caso, este método encuentra todas las coincidencias en el texto y las retorna en una lista.")
patron='ayuda'
busqueda=re.findall(patron,texto)
print(busqueda)
print(f"Longitud de la lista: {len(busqueda)}")
print()

print("Recorrer el texto y encontrar coincidencias mediante una iteración:")
for hallazgo in re.finditer(patron, texto):
    print(hallazgo)



print("\nPatrones especiales => patron=r'\d\d\d-\d\d\d-\d\d\d\d'")
texto="Llama al 564-535-6588 ya mismo"
patron=r'\d{3}-\d{3}-\d{4}'  #Utilizando cuantificadores
#patron=r'\d\d\d-\d\d\d-\d\d\d\d'
resultado=re.search(patron, texto)
print(resultado)
print("\n.group() retorna la coincidencia encontrada: ")
print(resultado.group())
print()


print("\nPatrones especiales utilizando compile => patron=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d)'")
texto=("Llama al 564-535-6588 ya mismo")
patron=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado=re.search(patron, texto)
print("\nre.compile() permite agrupar en grupos la coincidencia encontrada y acceder a estas agrupaciones mediante los indices de agrupacion: ")
print(resultado)
print(resultado.group())
print(resultado.group(1))
print(resultado.group(2))
print(resultado.group(3))
print()

print("\nPatrones especiales utilizando compile para una clave de acceso => patron=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d)'")
clave=input("Calve: ")
patron=r'\D{1}\w{7}'
resultado=re.search(patron, clave)
print(resultado)
print()

print("Utilizar el patron | para indicar que busque dos coincidencias si se cumple al menos una (OR)")
texto="No atendemos los lunes por la tarde "
buscar=re.search(r'lunes|martes',texto)
print(buscar)
texto="No atendemos los martes por la tarde "
buscar=re.search(r'lunes|martes',texto)
print(buscar)
texto="No atendemos los miercoles por la tarde "
buscar=re.search(r'lunes|martes',texto)
print(buscar)
print()

print("Uso de comodines en la busqueda")
buscar=re.search(r'demos',texto)
print(buscar)
print("\nBusca el caracter antes del comodin  => re.search(r'.demos',texto)")
buscar=re.search(r'.demos',texto)
print(buscar)
print("\nBusca los caracteres del comodin indicados por cada punto antes y despues")
buscar=re.search(r'...demos...',texto)
print(buscar)
print()

print("Buscar si un patron se encuentra al comienzo del string, en este caso \D  => NO numérico ")
buscar=re.search(r'^\D',texto)
print(buscar)
print()


print("Buscar si un patron se encuentra al comienzo del string, en este caso \D  => NO numérico ")
texto="3No atendemos los lunes por la tarde "
buscar=re.search(r'^\D',texto)
print(buscar)
print()

print("Buscar si un patron se encuentra al final del string, en este caso \D$  => NO numérico ")
texto="3No atendemos los lunes por la tarde"
buscar=re.search(r'\D$',texto)
print(buscar)
print()


print("Buscar si un patron se encuentra al final del string, en este caso \D$  => NO numérico ")
texto="No atendemos los lunes por la tarde4"
buscar=re.search(r'\D$',texto)
print(buscar)
print()

print("El uso de [] permite encontrar patrones que excluyan en este caso un caracter u patron indicado. En este caso crea una lista con todos los caracteres del texto excluyendo los espacios")
texto="No atendemos los lunes por la tarde"
buscar=re.findall(r'[^\s]',texto)
print(buscar)
print()

print("El uso de [] permite encontrar patrones que excluyan en este caso un caracter u patron indicado. Podemos decirle que nos muestre las palabras separadas por el espacio cada que sea encotrado utilizando el patron +")
print("Cada que se encuentre un espacio vacio, corta el grupo de palabras encontradas y las coloca en una lista.")
texto="No atendemos los lunes por la tarde"
buscar=re.findall(r'[^\s]+',texto)
print(buscar)
print()

print("Unir el listado de palabras encontradas mediante .join()")
print(''.join(buscar))
print()


print('''
Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).
Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.''')

print('''La expresión regular (re.match) permite verificar si el email dado cumple con el patrón especificado. Si coincide con el patrón, imprime "Ok"; de lo contrario, imprime "La dirección de email es incorrecta"\n''')

def verificar_email(email):
    # Utilizamos una expresión regular para verificar el formato del email.
    # El patrón busca una "@" seguida de cualquier texto, seguida de ".com" o ".com.br".
    patron = r'^[\w\.-]+@[\w\.-]+\.(com|com\.br)$'

    if re.match(patron, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


# Ejemplos de uso:
verificar_email("usuario@example.com")  # Debería imprimir "Ok"
verificar_email("usuario@example.com.br")  # Debería imprimir "Ok"
verificar_email("usuarioexample.com")  # Debería imprimir "La dirección de email es incorrecta"
verificar_email("usuario@example")  # Debería imprimir "La dirección de email es incorrecta"


print('''\nCrea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.
''')
def verificar_saludo(frase):
    # Utilizamos el método startswith para verificar si la frase comienza con "Hola".
    if frase.startswith("Hola"):
        print("Ok")
    else:
        print("No has saludado")

# Ejemplos de uso:
verificar_saludo("Hola, ¿cómo estás?")   # Debería imprimir "Ok"
verificar_saludo("Hola a todos")         # Debería imprimir "Ok"
verificar_saludo("Buenos días")          # Debería imprimir "No has saludado"
verificar_saludo("Adiós, hasta luego")    # Debería imprimir "No has saludado"


print("\nUtilizando módulo RE")
def verificar_saludo(frase):
    # Utilizamos re.match para buscar "Hola" al principio de la frase.
    if re.match(r'^Hola', frase):
        print("Ok")
    else:
        print("No has saludado")

# Ejemplos de uso:
verificar_saludo("Hola, ¿cómo estás?")   # Debería imprimir "Ok"
verificar_saludo("Hola a todos")         # Debería imprimir "Ok"
verificar_saludo("Buenos días")          # Debería imprimir "No has saludado"
verificar_saludo("Adiós, hasta luego")    # Debería imprimir "No has saludado"

print('''
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".''')

def verificar_cp(cp):
    # Utilizamos una expresión regular para verificar el formato del código postal.
    # El patrón busca dos caracteres alfanuméricos seguidos de cuatro dígitos.
    patron = r'^[A-Za-z]{2}\d{4}$'

    if re.match(patron, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


# Ejemplos de uso:
verificar_cp("AB1234")  # Debería imprimir "Ok"
verificar_cp("XY4567")  # Debería imprimir "Ok"
verificar_cp("12ABCD")  # Debería imprimir "El código postal ingresado no es correcto"
verificar_cp("ABCDE12")  # Debería imprimir "El código postal ingresado no es correcto"
