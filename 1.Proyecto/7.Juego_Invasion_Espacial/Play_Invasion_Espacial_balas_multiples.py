'''Crear la pantalla

pip install pygame

Cada cosa que suceda en la pantalla de pygame es un evento.

#DINAMICA DEL MOVIMIENTO
    #jugador_x+=0.1  #Si queremos que nuestro jugador se mueva cada 0.1px hacia la derecha mientras el loop este activo ejecutandose
    #jugador_x-= 0.1  # Si queremos que nuestro jugador se mueva cada 0.1px hacia la izquierda mientras el loop este activo ejecutandose
    #jugador_y+=0.1 # Si queremos que nuestro jugador se mueva cada 0.1px hacia abajo mientras el loop este activo ejecutandose
    #jugador_y-=0.1 # Si queremos que nuestro jugador se mueva cada 0.1px hacia la arriba mientras el loop este activo ejecutandose

Ejecutable =>
*   Convertir las fuentes de tipo Sting a objetos Bytes
*   Utilizar pyinstaller

#Fuentes => https://www.download-free-fonts.com/download/2045/8e59a771195256d50768d69c39a61874
'''
import pygame
import random
import math
from pygame import mixer # Permite trabajar con sonidos
import io

# Funcion para exportar ejecutable
def fuente_bytes(fuente):
    with open(fuente,'rb') as f:
        ttf_bytes = f.read()
        return io.BytesIO(ttf_bytes)

#Inicializo pygame
pygame.init()

#Crear la pantalla
pantalla=pygame.display.set_mode((800,600))  #Defino el alto y ancho de la pantalla en una tupla (higth, weigth)

# Titulo, icono e imagen de fondo
# Página de iconos => https://www.flaticon.es/  ; Recomendable 32px para iconos y 64px para iconos del juego
pygame.display.set_caption("Invasión Espacial")
icono=pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo=pygame.image.load('Fondo.jpg')

# Musica de fondo
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.5)  # Fijar volumen, en este caso la mitad del volumen que tenia.
mixer.music.play((-1)) # -1 significa que se va a repetir cada vez que termine, damos play

# VARIABLES DEL JUGADOR
# Cargar Icono del jugador
# El icono jugador tiene 64 pixeles, la mitad es 32px. Por lo tanto si quiero ubicarlo en el centro => La pantalla tiene 800px, la mitad es 400 px, si queremos ubicar el icono en el medio es igual a 400px - 32px = 368px
img_jugador=pygame.image.load("cohete.png")
jugador_x=368
jugador_y=500  #La altura seria 600px-64px = 536px => Opcional 500px
jugador_x_cambio=0

#Variables Enemigos
#Valores aleatorios posicion del enemigo que abarca el tamaño de la pantalla
img_enemigo=[]
enemigo_x=[]
enemigo_y=[]
enemigo_x_cambio=[]
enemigo_y_cambio=[]
cantidad_enemigos=8

#Creamos un array de enemigos
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

#Variables de la bala
balas=[]
img_bala=pygame.image.load("bala.png")
bala_x= 0
bala_y= 500         #   Altura donde esta la nave desde donde sale la bala
bala_x_cambio=0     #   Valor de x no se modifica
bala_y_cambio=3
bala_visible=False

# Puntaje
puntaje = 0
# Fuente como bytes
fuente_como_bytes=fuente_bytes("FreeSansBold.ttf")
fuente =pygame.font.Font(fuente_como_bytes,32)

#Mostrar el puntaje en pantalla, fuente de la letra
#fuente =pygame.font.Font('freesansbold.ttf',32)


#Coordenadas del texto
texto_x=10
texto_y=10

# Funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto= fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))  #Renderizar o imprimir en pantalla
    pantalla.blit(texto,(x,y)) #Mostrar en pantalla de pygame


# FUNCION DEL JUGADOR
def jugador(x,y):
    #Ubicamos el icono de la imagen del jugador mediante metodo blit(), inicialmente en la posicion (x,y)
    pantalla.blit(img_jugador,(x,y))

# FUNCION ENEMIGO
def enemigo(x,y,en):
    pantalla.blit(img_enemigo[en],(x,y))

# FUNCION DISPARAR BALA
def dispar_bala(x,y):
    global bala_visible  #Variable definida globalmente para ser utilizada cuando se dispare la bala
    bala_visible =True
    pantalla.blit(img_bala,(x+16,y+10)) # +16 en el eje x para que quede en el centro de la nave y +10 en el eje y.

# Funcion para detectar colisiones
def hay_colision(x_1,x_2,y_1,y_2):
    # Evaluar potencias =>  math.pow(x_2-x_1,2)
    distancia = math.sqrt(math.pow(x_2-x_1,2)+math.pow(y_2-y_1,2))
    if distancia < 27:  #Valor 27 (px) es suficiente para indicar que la bala ha tocado al enemigo
        return  True
    else:
        return  False

#Texto final del juego
fuente_final =pygame.font.Font('freesansbold.ttf',40)
def texto_final():
    mi_fuente_final=fuente_final.render("GAME OVER",True, (255,255,255))
    pantalla.blit(mi_fuente_final,(220,200)) #Mostramos el mensaje final en el centro


#Loop del juego para que la pantalla este abierta, mientras el usuario no presiona el boton cerrar => Evento QUIT
se_ejecuta=True
while se_ejecuta:
    # Cambiar el fondo de la pantalla  RGB, se recomienda hacerlo dentro del loop cuando se detecta un evento
    # Páginas de colores  => https://www.colorspire.com/rgb-color-wheel/
    # pantalla.fill((205, 144, 228))  # Rellenar con colores de fondo

    # Rellenar con imagen de fongo, esto retarda la iteracion mientras carga la imágen
    pantalla.blit(fondo, (0,0))

    for evento in pygame.event.get(): #Otiene el listado de eventos de la cola en el bucle de eventos => pygame.event.get()

        # EVENTO DE CERRAR PANTALLA
        #QUIT es un EVENTO que se ejecuta cuando se presiona sobre el boton de cerrar en la pantalla
        if evento.type==pygame.QUIT:
            se_ejecuta=False

        #Evento tecla presionada
        if evento.type==pygame.KEYDOWN:
            #Tenemos la opción de validar todas las teclas, como se utiliza una imagen en la pantalla se aumenta el movimiento de 0.3 a 1.
            if evento.key==pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key==pygame.K_RIGHT:
                jugador_x_cambio = 1
            # Disparar bala
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
            balas.append(nueva_bala)

        #EVENTO que verifica cuando la tecla ha sido levantada luego de ser presionada
        if evento.type==pygame.KEYUP:
            if evento.key==pygame.K_LEFT or evento.key== pygame.K_RIGHT:
                jugador_x_cambio=0

    # MODIFICAR POSICIÓN DEL JUGADOR
    #A la posicion de la x dentro del loop le sumamos o restamos los valores del cambio en la posicion de x segun la tecla presionada
    jugador_x +=jugador_x_cambio

    # MANTENER EL JUGADOR DENTRO DE LOS BORDES DE LA PANTALLA
    if jugador_x<=0:
        jugador_x=0
    elif jugador_x >= 736:  #800px-64px = 763px
        jugador_x=736

    # MODIFICAR POSICIÓN DEL ENEMIGO => Recorremos el array de enemigos
    # A la posicion de la x dentro del loop le sumamos o restamos los valores del cambio en la posicion de x segun la tecla presionada
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]

        # Fin del juego si un enemigo alcanza una altura de 500
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k]=1000   # Colocamos una altura de 1000 para que ya no se muestren los enemigos
            texto_final()
            balas.clear()
            break #Rompemos o terminamos el ciclo


        # MANTENER EL ENEMIGO DENTRO DE LOS BORDES DE LA PANTALLA
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e]+=enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:  # 800px-64px = 763px
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], bala["x"], enemigo_y[e], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e],e)

    # Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    if bala_y <= -64: #El tamaño de la bala
        bala_y=500
        bala_visible=False
        puntaje +=1
        print(puntaje)

    if bala_visible:
        dispar_bala(bala_x,bala_y)
        bala_y-=bala_y_cambio

    # Inicializamos la posicion inicial del icono del jugaror + el movimiento en el eje x
    jugador(jugador_x, jugador_y)

    # Mostrar puntaje
    mostrar_puntaje(texto_x,texto_y)

    # ACTUALIZAR PANTALLA
    pygame.display.update()