import cv2
import  face_recognition as fr
import os
import numpy
from datetime import datetime

#Crear base de datos
ruta='Empleados'
mis_imagenes=[]
nombres_empleados=[]
lista_empleados=os.listdir(ruta)
print(lista_empleados)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')  # leer la imagen, se crea con la ruta dinamicamente de la imagen
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0]) # splitext retorna una tupla con: (nombre_archivo, extension_archivo)

print(nombres_empleados)


#Codificar imagenes
def codificar(imagenes):
    #Crear una lista nueva
    lista_codificada=[]
    #Pasar todas las imágenes
    for imagen in imagenes:
        imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        #Codificar
        codificado=fr.face_encodings(imagen)[0]
        #Agregar a la lista
        lista_codificada.append(codificado)
    #Devolver lista codificada
    return lista_codificada

#Registrar los ingresos
def registrar_ingresos(persona):
    f=open('registro.csv','r+') #r+ nos permite leer y escribir en el archivo
    lista_datos=f.readlines() #leer todas las lineas del archivo de texto
    nombres_registro=[]
    for linea in lista_datos:
        ingreso=linea.split(',')
        nombres_registro.append(ingreso[0])  #Guarda el nombre de la persona registrada

    if persona not in nombres_registro:
        ahora=datetime.now()
        string_ahora=ahora.strftime('%H:%M:%S')  #Variable donde se almacena la hora con formato H:M:S
        f.writelines(f"\n{persona},{string_ahora}")

lista_empleados_codificada=codificar(mis_imagenes)
print(f"Longitud lista de empleados: {len(lista_empleados_codificada)}")

#Tomar una imagen de camara web
captura = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Leer imagen de la camara
exito, imagen=captura.read()  #Exito es un booleana que indica si se pudo o no tomar la imagen
if not exito:
    print("No se ha podido tomar la captura")
else:
    #Reconocer cara en captura
    cara_captura=fr.face_locations(imagen)
    #Codificar cara capturada
    cara_captura_codificada=fr.face_encodings(imagen,cara_captura)
    #Buscar coincidencias
    for caracodif, caraubi in zip(cara_captura_codificada, cara_captura):
        coincidencias= fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada,caracodif)
        print(f"Distancia: {distancias}")

        indice_coincidencia=numpy.argmin(distancias)  #numpy.argmin es un metodo que obtiene de varios valores, el numero menor
        print(f"Indice de coincidencia: {indice_coincidencia}")
        #Mostrar coincidencias si las hay
        if distancias[indice_coincidencia] >0.6:
            print("No coincide con ninguno de nuestros empleados")
        else:
            #Buscar el nombre del empleado encontrado
            nombre=nombres_empleados[indice_coincidencia]
            print(f"Bienvenido al trabajo {nombre}")

            #Obtener informacion de la ubicacion de la cara ubicada
            y1,x2,y2,x1= caraubi
            cv2.rectangle(imagen,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(imagen,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED) #Rectangulo de color verde para añadir el nombre.
            cv2.putText(imagen,nombre, (x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255.255,255),2)

            #Registrar ingresos de las personas
            registrar_ingresos(nombre)

            #Mostrar la imagen obtenida
            cv2.imshow('Imagen web',imagen)
            #Mantener ventana abierta
            cv2.waitKey(0)


