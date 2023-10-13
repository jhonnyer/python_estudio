#Juego ahorcado
from random import *

lista_palabras=['panaderia','dinosaurio','helipuerto','tiburon']
letras_correctas=[]
letras_incorrectas=[]
intentos=6
aciertos=0
juego_terminado=False

def elegir_palabra(lista_palabras):
    palabra_elegida=choice(lista_palabras)
    letras_unicas=len(set(palabra_elegida)) #Verificar las letras unicas que tiene la palabra y cuantas letras son
    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida=''
    es_valida=False
    abecedario ='abcdefghijklmnopqrstuvwxyz'
    while not es_valida:
        letra_elegida=input("Elige una letra: ").lower()
        #Verifica si la letra elegida esta dentro del abecedario y si la longitud ingresada en el input es de un caracter
        if letra_elegida in abecedario and len(letra_elegida)==1:
            es_valida=True
        else:
            print("No has elegigo una letra correcta")
    return letra_elegida

def verificar_letra_ahorcado(letra_elegida, palabra_oculta, vidas, aciertos):
    fin=False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        aciertos+=1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra, intenta con otra")
    else:
        #Opcional que no repita letras erroneas escogidas anteriormente
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
        '''if letra_elegida not in letras_incorrectas:
            letras_incorrectas.append(letra_elegida)
            vidas-=1
        else:
            print("Ya has elegido erroneamente esa letra, intenta con otra")'''
    if vidas == 0:
        fin=perder()
    elif aciertos==letras_unicas:
        fin=ganar(palabra_oculta)

    return vidas, fin, aciertos

def perder():
    print("Has perdido, te has quedado sin vidas")
    print("La palabra oculta era: "+palabra)
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones, has encontrado la palabra! :)")
    return True

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta=[]
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))



#Invocar Función para elegir la palabra
palabra, letras_unicas=elegir_palabra(lista_palabras)

while not juego_terminado:
    print('\n'+'*'*20+'\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    # Opcional que la lista de letras_incorrectas, no contenga letras escogidas anteriormente
    #print('Letras incorrectas: '+'-'.join(list(set(letras_incorrectas))))
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print('\n' + '*' * 20 + '\n')
    letra=pedir_letra()
    #Coincidencias equivale a aciertos
    intentos, terminado, aciertos=verificar_letra_ahorcado(letra,palabra, intentos, aciertos)
    juego_terminado=terminado