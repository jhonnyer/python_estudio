import bs4  #Permite crear un objeto BeautifulSoup para poder navegar sobre el texto de la pagina y obtener el resultado deseado
import  requests

print("Pasarle un parametro a una ruta")
ruta='http://books.toscrape.com/catalogue/page-{}.html'
print(ruta.format('15'))
print("FIN")

print("\nRecorrer paginas")
for n in range(1,11):
    print(ruta.format(n))

print("\nObtener información de los libros, sus titulos y demás...")
resultado=requests.get(ruta.format('1'))
sopa=bs4.BeautifulSoup(resultado.text,'lxml')
print(f"{len(sopa.select('.product_pod'))} Libros encontrados\n")
libros=sopa.select('.product_pod')
print("\nImprimir libro en la posicion '0'")
print(libros[0])

print("\nImprimir libro en la posicion '0' y la clase 'star-rating Three'. En este caso, cuando se tiene varias clases con espacio, se colocan separadas con punto (.)")
print(libros[0].select('.star-rating.Three'))

print("\nImprimir el titulo del libro en la posicion '0'")
print(libros[0].select('a')[1]['title'])

print("\nCombinar busqueda anterior en un bucle FOR para encontrar los libros con mejor rating (estrellas) tiene\n")
titulos_rating_alto=[]

#Iterar paginas
for pagina in range(1,51):
    #Crear sopa en cada pagina
    url_pagina=ruta.format(pagina)
    resultado=requests.get(url_pagina)
    sopa=bs4.BeautifulSoup(resultado.text,'lxml')

    #Seleccionar datos de los libros
    libros =sopa.select('.product_pod')

    #Iterar libros
    for libro in libros:
        #Chequear que tegan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) !=0 or len(libro.select('.star-rating.Five')) !=0:
            #Guardar titulo en variable
            titulo_libro=libro.select('a')[1]['title']
            #Agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

#Ver libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)