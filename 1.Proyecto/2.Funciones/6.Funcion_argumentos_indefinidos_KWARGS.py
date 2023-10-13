#**kwargs
#Se indica que es un kwargs porque empieza con ** y trabaja con diccionarios
#Los argumentos con palabras clave (keyword arguments, abreviado kwargs),
# sirven para identificar el argumento por su nombre, independientemente de la posición en la que se pasen a su función.
# Si no se conoce de antemano su cantidad, se utiliza el parámetro **kwargs que los agrupa en un diccionario

#Al igual que para *args, el nombre **kwargs no es mandatorio pero si es sugerido como buena práctica. Cualquier nombre iniciado en ** referirá a estos argumentos de cantidad variable.
# => def atributos_persona(**kwargs):
#atributos_persona(ojos= "azules" , pelo= "corto") => kwargs = {'ojos': 'azules', 'pelo': 'rubio'}

print("Ejemplo de uso de los Kwargs y su tipo")
def suma(**kwargs):
    print(kwargs)
    print(type(kwargs))
suma(x=3,y=5,z=2)
print()

##################################################
print("Ejemplo de uso de los Kwargs, acceso a sus datos y operacion aritmetica")
def suma(**kwargs):
    total=0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total+=valor
    return total

x=3
y=5
z=2
resultado=suma(x=x,y=y,z=z)
print(f"El resultado de la suma de los números ingresados {x,y,z} es {resultado}")
print()

##################################################
#El orden de los argumentos son: Argumentos normales, *arg. **kwargs
print("Ejemplo de uso de los argumentos normales, *args y **kwargs, acceso a sus datos y operacion aritmetica:\n")
def suma_argumentos(num1,num2,*args,**kwargs):
    print(f"El primer valor es: {num1}")
    print(f"El segundo valor es: {num2}")
    total=num1+num2
    lista=[num1, num2]
    print(f"Argumentos args")
    for arg in args:
        print(f"args= {arg}")
        lista.append(arg)
        total=total+arg

    print(f"Argumentos **kwargs\n")
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        lista.append(valor)
        total+=valor
    print(f"El resultado de la suma de los números ingresados {lista} es {total}\n")
    return total

resultado=suma_argumentos(15,34,54,76,345,x=3,y=5,z=2)
print()
print("Utilizar funcion suma_argumentos() sin enviar args o kwargs")
resultado=suma_argumentos(15,34,)
print()

print("Utilizar funcion suma_argumentos() enviando estructura de datos de args y kwargs")
args=[100,200,300,400]
kwargs={'x':1,'y':2,'z':3}
resultado=suma_argumentos(15,34,*args,**kwargs)
print()


print("Utilizar funcion suma_argumentos() enviando estructura de datos  kwargs")
args=[100,200,300,400]
kwargs={'x':1,'y':2,'z':3}
resultado=suma_argumentos(15,34,**kwargs)
print()

####################################
print("Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.")
def cantidad_atributos(**kwargs):
    return len(kwargs)

print(f"Cantidad de atributos enviados en la funcion: {cantidad_atributos(z=21,y=2)}")


######################################
print("\nCrea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.")
def lista_atributos(**kwargs):
    lista=[]
    for clave, valor in kwargs.items():
        lista.append(valor)
    return lista

print(lista_atributos(x=1,y=54,z='Fin'))


######################################
print("\nCrea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.")
print("Utilizando comprension de lista")
def lista_atributos(**kwargs):
    lista=[valor for clave, valor in kwargs.items()]
    return lista

print(lista_atributos(x=1,y=54,z='Fin'))
print()

#Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:
#Características de {nombre}:
#{nombre_argumento}: {valor_argumento}
#{nombre_argumento}: {valor_argumento}
#etc...
print('''Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
''')

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")

describir_persona("María", color_ojos="azules", color_pelo="rubio")
