'''
    Reconocimiento facial o biometría facial

Utilizado para:

    * desbloqueo telefónico
    * fuerzas de seguridad
    * control en aeropuertos
    * busqueda de desaparecidos
    * derecho de admisión
    * operaciones bancarias
    * monitoreo en casinos
    * asistencia laboral, etc

PASOS:

1. Reconocimiento facial
2. análisis facial
3. convertir imagen en datos
4. Buscar coincidencias

Instalar recurso extra => Compilador C version comunitaria=> https://visualstudio.microsoft.com/es/downloads/
Seleccionar la opción =>
 - Desarrollo de escritorio de .NET
 - Desarrollo de la plataforma universal de Windows
 - Desarrollo para el escritorio con C++

Bibliotecas necesarias

* cmake
* dlib
* face-recognition  => Reconocimiento facial
* numpy => Biblioteca de manejo de números
* opencv-python
'''

import cv2
import face_recognition as fr

#Cargar imagenes
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba=fr.load_image_file('FotoB.jpg')

#Pasar imagen a rgb
foto_control= cv2.cvtColor(foto_control,cv2.COLOR_BGR2RGB)
foto_prueba= cv2.cvtColor(foto_prueba,cv2.COLOR_BGR2RGB)

#localizar cara control
lugar_cara_A=fr.face_locations(foto_control)[0] #[0] indica que estamos tomando el primer elemento de esa imagen
cara_codificado_A=fr.face_encodings(foto_control)[0]
print(lugar_cara_A)  # Muestra parametros de la cara primer posicion, coordenadas

#Mostrar rectangulo
cv2.rectangle(foto_control,
              (lugar_cara_A[3],lugar_cara_A[0]),  #Posicion rectangulo eje x
              (lugar_cara_A[1],lugar_cara_A[2]),  # Posicion rectangulo eje y
              (0,255,0), #Rectangulo de color verde
              2)  #Tamaño rectangulo 2

#localizar cara prueba
lugar_cara_B=fr.face_locations(foto_prueba)[0] #[0] indica que estamos tomando el primer elemento de esa imagen
cara_codificado_B=fr.face_encodings(foto_prueba)[0]
print(lugar_cara_B)  # Muestra parametros de la cara primer posicion, coordenadas

#Mostrar rectangulo
cv2.rectangle(foto_prueba,
              (lugar_cara_B[3],lugar_cara_B[0]),  #Posicion rectangulo eje x
              (lugar_cara_B[1],lugar_cara_B[2]),  # Posicion rectangulo eje y
              (0,255,0), #Rectangulo de color verde
              2)  #Tamaño rectangulo 2


#Realizar comparación, entre más grande el valor de tolerancia mayor va a ser la coincidencia y puede generar resultados errones
#resultado=fr.compare_faces([cara_codificado_A],cara_codificado_B, 0.3) #el valor decimal definido indica la tolerancia entre la distancia de comparacion de la foto,se puede dejar por defecto o añadir un valor
#resultado=fr.compare_faces([cara_codificado_A],cara_codificado_B, 0.9) #el valor decimal definido indica la tolerancia entre la distancia de comparacion de la foto,se puede dejar por defecto o añadir un valor
resultado=fr.compare_faces([cara_codificado_A],cara_codificado_B) #el valor decimal definido indica la tolerancia entre la distancia de comparacion de la foto,se puede dejar por defecto o añadir un valor
print(resultado)

#Medida de la distancia
distancia = fr.face_distance([cara_codificado_A],cara_codificado_B)
print(distancia)

#mostrar resultado en pantalla
cv2.putText(foto_prueba,
            f"{resultado} {distancia.round(2)}",
            (50,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,255,0),
            2) #Ubicacion del texto

#mostrar imagenes
cv2.imshow('Foto Control',foto_control)
cv2.imshow('Foto Prueba',foto_prueba)


#Mantener el programa abierto
cv2.waitKey(0)
