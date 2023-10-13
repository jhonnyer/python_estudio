'''
Web Scraping => Permite extraer informacion de una página teniendo en cuenta los conceptos de:

*   html  => Estructura y contenido de la pagina web (informacion, imagenes, textos, etc)
*   css  => Diseño y estilo de la página web
*   javascript => Elementos interactivos de la página web

 - Reglas del Web Scraping  => Permisos páginas web
 - limitaciones del web scraping

'''
import bs4  #Permite crear un objeto BeautifulSoup para poder navegar sobre el texto de la pagina y obtener el resultado deseado
import  requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")
print(type(resultado))  #Muestra el tipo del request solicitado
print(resultado.text)   #Muestra el contenido del resultado como texto
print()


print("*"*50)
print("*"*19+" INICIO lxml "+"*"*18)
print("*"*50)
print("bs4.BeautifulSoup(resultado.text, 'lxml') => Permite navegar sobre los elementos")
sopa=bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa)
print()

print("*"*50)
print("Buscar titulo de la página por medio del método select y la propiedad html title, retorna una lista con los elementos encontrados")
print("*"*50)
print(sopa.select('title'))
print()

print("*"*50)
print("Buscar los elementos <h1> de parrafos en la página por medio del método select y la propiedad html 'h1'")
print("*"*50)
print(sopa.select('h1'))
print()
print(sopa.select('h1')[0]) #Muestra de la lista de elementos encontrados el correspondiente a la posicion 0
print(sopa.select('h1')[0].getText())  #Quitarle la etiqueta (h1) al elemento encontrado
print()

print("*"*50)
print("Buscar los elementos <h1> de parrafos en la página por medio del método select y la propiedad html 'h1'")
print("*"*50)
# Encuentra todos los elementos <p> en el objeto BeautifulSoup
parrafos = sopa.find_all('h1')

# Itera a través de los párrafos e imprime su contenido
for parrafo in parrafos:
    print(parrafo.text)

print("FIN")