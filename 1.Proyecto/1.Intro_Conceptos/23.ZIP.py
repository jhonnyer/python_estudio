#La función zip( ) crea un iterador formado por los elementos agrupados del mismo índice provenientes de dos o más iterables. Zip deriva de zipper (cremallera o cierre), de modo que es una analogía muy útil para recordar
#Combina dos o más listas entrelanzandolas por medio de tuplas en orden
#Consideraciones: Las listas pueden ser de diferentes tamaños, en este caso ZIP considera el largo de la lista mas corta, los demás datos los va a ignorar

print("Uzo de zip y verificacion de datos, para observarlo debemos caster el ZIP a una lista")
nombres=['Ana', 'Hugo','Valeria', 'Jhonnyer']
edades=[56,87,23]
combinados=zip(nombres,edades)
print("ZIP sin castear a lista")
print(combinados)  # Para verlo se debe castear en una lista
print("ZIP  casteado a una lista")
print(list(combinados))  # Para verlo se debe castear en una lista


print("\nUzo de zip con tres listas, en este caso genera una tupla mas larga")
nombres=['Ana', 'Hugo','Valeria', 'Jhonnyer']
edades=[56,87,23]
ciudades=["Medellin", 'Cali','Popayan']
combinados=list(zip(nombres,edades, ciudades))
print(combinados)  # Para verlo se debe castear en una lista
print()


print("\nRecorrer lista de tupla generada con zip\n")
for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
print()

####################
#Muestra en pantalla frases como la del siguiente ejemplo:
#La capital de Alemania es Berlín
print("Ejemplo tuplas con ZIP\n")
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinados=list(zip(capitales, paises))
for capital, pais in combinados:
    print(f"La capital de {pais} es {capital}")
print()

#########################
#Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:
#uno / um / one
#dos / dois / two
#tres / três / three
#cuatro / quatro / four
#cinco / cinco / five
#El resultado deberá seguir la estructura:
#[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]

print("Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros")
uno= ['uno', 'um','one']
dos= ['dos','dois','two']
tres= ['tres','três','three']
cuatro= ['cuatro','quatro','four']
cinco= ['cinco','cinco','five']
objeto_trad={
    'uno':uno,
    'dos':dos,
    'tres':tres,
    'cuatro':cuatro,
    'cinco':cinco
}

# Listas separadas para cada idioma
lista_espanol = []
lista_portugues = []
lista_ingles = []

print(objeto_trad)
print(type(objeto_trad))
for numero, traducciones in objeto_trad.items():
    lista_espanol.append(traducciones[0])
    lista_portugues.append(traducciones[1])
    lista_ingles.append(traducciones[2])

print(lista_espanol);
print(lista_portugues)
print(lista_ingles)

numeros = list(zip(lista_espanol,lista_portugues,lista_ingles))
print(numeros)