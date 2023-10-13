import bs4  #Permite crear un objeto BeautifulSoup para poder navegar sobre el texto de la pagina y obtener el resultado deseado
import  requests

resultado =requests.get("https://www.escueladirecta.com/courses")
sopa=bs4.BeautifulSoup(resultado.text,'lxml')

imagenes = sopa.select('img')
print("\nTodas las imagenes sin patron de busqueda\n")
for img in imagenes:
    print(img)

print("\nPatron de busqueda encotrado => class='course-box-image'\n")
imagenes = sopa.select('.course-box-image')
for img in imagenes:
    print(img['src'])  #Obtener unicamente el link ubicado en el elemento src de las etiquetas


print("\nObtener response y la imagen del elemento. Almacenarla en el ordenador'\n")
imagen=sopa.select('.course-box-image')[0]['src']
imagen_curso1=requests.get(imagen)
print(imagen_curso1)
print(imagen_curso1.content) #Obtiene los bytes de la imagen
f=open('mi_imagen.jpg','wb') #wb significa escribir binario
f.write(imagen_curso1.content)
f.close()


