print('''\nEscribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta función es devolver True si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas
''')

def procesar_numeros_vecinos(*args):
    contador=0
    for arg in args:
        #Verificar dato ultimo si no hay más posiciones a evaluar, ejemplo cero posicion ultima
        if contador+1==len(args):
            return False
        elif args[contador] == 0 and args[contador+1] == 0:
            print(f"Aparece dos ceros repetidos en la posicíón: {contador} de los datos ingresados+-")
            return True #Si aparece una coincidencia termina el bucle
        else:
            contador+=1 #Garantiza continuar la iteración
    return False


print(procesar_numeros_vecinos(5,6,1,0,0,9,3,5))
print(procesar_numeros_vecinos(6,0,5,1,0,3,0,1,0))