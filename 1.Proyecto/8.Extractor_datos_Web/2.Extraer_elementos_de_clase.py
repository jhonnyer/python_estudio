'''
soup.select('div')              => Todos los elementos con etiqueta div
soup.select('#estilo_4')        => Elementos que contengan id= 'estilo4'
soup.select('.columna_der')     => Elementos que contengan class='columna der'
soup.select('div span')         => Cualquier elemento llamado 'span' dentro de un elemento 'div
soup.select('div>span')         => Cualquier elemento llamado 'span' directamente dentro de un elemento 'div', sin nada en el medio
'''

import bs4  #Permite crear un objeto BeautifulSoup para poder navegar sobre el texto de la pagina y obtener el resultado deseado
import  requests

resultado =requests.get("https://www.openstack.org/")
sopa=bs4.BeautifulSoup(resultado.text,'lxml')

columna=sopa.select('p')[3].getText()
print(columna)


print("\nObtener una clase")
clase= sopa.select('.twros-btn-wrapper')
print(clase)


print("\nObtener un elemento h2 dentro de un div")
clase= sopa.select('.twros-text h2')
print(clase)


print("\nRecorrer la lista de elementos h2 dentro de un div e imprimir el texto de cada uno")
lista= sopa.select('.twros-text h2')

for l in lista:
    print(l.getText())
