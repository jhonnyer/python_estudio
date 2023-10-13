#Slicing rebanar o extraer un string de una cadena de caracteres, ejemplos:
#[3] => Extraer el caracter en el indice 3
#[3:] => Extraer desde el indice 3, incluyendolo hasta el final
#[:5] => Extraer desde el indice 0, hasta el indice 5 sin incluirlo
#[3:5] => Extraer desde el indice 3 incluyendolo, hasta el indice 5 sin incluir.
#[3:5:2] => Extraer desde el indice 3 incluyendolo, hasta el indice 5 sin incluir. El tercer valor nos indica cada cuantos caracteres se va a seleccionar nuestro fragmento.
#[:] => Todos los caracteres

texto="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
print("TEXTO A FORMATEAR: "+texto)
fragmento= texto[2];
print("\nSlicing un solo caracter")
print(fragmento);

fragmento= texto[5:];
print("\nSlicing desde el indice 5 hasta el final")
print(fragmento);

fragmento= texto[:5];
print("\nSlicing desde el indice 0  hasta el indice 5")
print(fragmento);

fragmento= texto[2:7];
print("\nSlicing desde el indice 2  hasta el indice 7")
print(fragmento);

fragmento= texto[2:10:2];
print("\nSlicing desde el indice 2  hasta el indice 10, tomando caracteres cada 2 posiciones")
print(fragmento);

fragmento= texto[::3];
print("\nSlicing desde el indice 0  hasta el indice final, tomando caracteres cada 3 posiciones")
print(fragmento);

fragmento= texto[::-1];
print("\nSlicing que toma en este caso toda la cadena pero al revez")
print(fragmento);

fragmento= texto[::-3];
print("\nSlicing que toma en este caso toda la cadena tomando caracteres cada 3 posiciones")
print(fragmento);