'''
Bibliotecas

* pyttsx3 => Permite a python hablar con nosotros
* speedch_recognition => Permite traducir el sonido de la voz humana a texto
* webbrowser => Para manipular un navegdor WEB
* pywhatkiy => Conectar codigo con muchos sitios web como Youtube, Google y más
* yfinance => Buscar información en el mercado de la bolsa
* pyjokes => Libreria de chistes para que el asistente no sea nada aburrido
* wikipedia => Buscar de todo en la web

Librerias requeridas:

* pip install flask
pip install PyAudio


En caso de error:
Abre CMD en Windows (o la terminal en Mac) y escribe lo siguiente:
pip install pipwin
pipwin install PyAudio
'''
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser #Ya viene incluida en python
import datetime
import  wikipedia

#OPCIONES DE VOZ DISPONIBLES ENCONTRADAS
id1='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

def transformar_audio_en_texto():
    #Almacenar recognizer en variable
    r=sr.Recognizer()

    #Configurar el microfono, origen es un objeto del microfono
    with sr.Microphone() as origen:

        #Tiempo de espera para que haya un momento de espera cuando se active el microfono
        r.pause_threshold=0.8

        #informar que comenzo la grabación
        hablar("Por favor, dime en que te puedo ayudar")
        #print("Ya puedes empezar a hablar")

        #Guardar lo que escuche como audio
        audio=r.listen(origen)

        try:
            #Buscar en google
            pedido=r.recognize_google(audio,language="es-col")

            #Prueba de que pudo ingresar
            print("Digiste: "+pedido)

            #Devolver pedido
            return pedido
        #En caso de que no comprenda el audio
        except sr.UnknownValueError:
            #Prueba de que no comprendio el audio
            print("Ups, no entendi")
            #Devolver error
            return "Sigo esperando"

        #En caso de que no puede resolver el pedido
        except sr.RequestError:
            #Prueba de que no comprendio el audio
            print("Ups, no hay servicio")
            #Devolver el error
            return "Sigo esperando"

        #Error inesperado
        except:
            # Prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")
            # Devolver el error
            return "Sigo esperando"

#Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #Encender el motor de pyttsx3
    engine=pyttsx3.init()
    #Setear una voz a mi funcion de hablar
    engine.setProperty('voice',id1)

    #Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#VER VOCES QUE CUENTA MI SISTEMA
#engine=pyttsx3.init()
#for voz in engine.getProperty('voices'):
#    print(voz)


#INFORMAR EL DIA DE LA SEMANA
def pedir_dia():
    #Crear variable con datos de hoy
    dia=datetime.date.today()
    print(dia)

    #Crear variable para el dia de semana
    dia_semana=dia.weekday()  #Muestra el indice
    print(dia_semana)
    #Diccionario con nombre de días
    calendario={
        0:'Lunes',
        1:'Martes',
        2:'Miércoles',
        3:'Jueves',
        4:'Viernes',
        5:'Sabado',
        6:'Domingo',
    }

    #Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

#Informar hora
def pedir_hora():
    #Crear variable con datos de hora
    hora=datetime.datetime.now()
    #Dar formato de hora
    hora=f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    #decir la hora
    hablar(hora)

def saludo_inicial():
    #Crear variable con datos de hora
    hora=datetime.datetime.now()
    if hora.hour<6 or hora.hour>20:
        momento="Buenas noches"
    elif 6<= hora.hour <13:
        momento="Buen día"
    else:
        momento="Buenas tardes"
    #Decir el saludo
    hablar(f'{momento}, soy tu asistente personal.')


#Funcion central del asistente
def pedir_cosas():
    #Activar saludo inicial
    saludo_inicial()

    #Menu opciones
    #Variable de corte
    comenzar=True
    while comenzar:
        #Activar el micro y guardar el pedido en un string
        pedido= transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar("Con gusto, estoy abriendo youTube")
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Con gusto, estoy abriendo el navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'abrir correo' in pedido:
            hablar('Con gusto, estoy abriendo el correo')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar("Buscando en wikipedia")
            pedido=pedido.replace('buscar en wikipedia','')
            wikipedia.set_lang('es')
            resultado=wikipedia.summary(pedido, sentences=1) #sentences 1 solo muestra la primer linea del texto encontrado
            hablar('Wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'buscar en internet' in pedido:
            hablar('Ok, ya mismo lo busco')
            pedido=pedido.replace("buscar en internet",'')
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion=pedido.split('de')[-1].strip() #ME quedo con la accion que quiero encontrar y elimino espacios en blanco
            cartera={
                'Apple':'APPL',
                'Amazon':'AMZN',
                'Google':'GOOGL'
            }
            try:
                accion_buscada=cartera[accion]
                accion_buscada=yf.Ticker(accion_buscada)
                precio_actual=accion_buscada.info['regularMarketPrice']
                hablar(f"La encontré, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdón no la he encontrado")
                continue
        elif 'salir' or 'adios' in pedido:
            hablar("Ok, hasta luego, me voy a descansar, cualquier cosa me avisas")
            break

pedir_cosas()


