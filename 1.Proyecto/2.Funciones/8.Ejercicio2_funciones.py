print('''Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro, y que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
Por ejemplo si al invocar esta función pasamos la palabra "entretenido" , debería devolver 
['d' , 'e' , 'i' , 'n' , 'o' , 'r' , 't'] ''')

def procesar_texto(texto):
    conjunto=set()
    for letra in texto:
        conjunto.add(letra)
    lista=list(conjunto)
    lista.sort()
    return lista

texto = input("Ingresa una palabra o el texto que quieras: ")
respuesta=procesar_texto(texto)
print(respuesta)