texto=input("Ingresa el parrafo de un texto: \n")
texto=texto.lower();

print("Ingrese 3 letras de su elección")
letra1=input("Primer letra: ").lower();
letra2=input("Segunda letra: ").lower();
letra3=input("Tercer letra: ").lower();
print()
print(texto)
print()
print("Conteo del número de veces que aparece las letras elegidas")
print(f"La letra o frase {letra1} aparece {texto.count(letra1)} veces")
print(f"La letra o frase {letra2} aparece {texto.count(letra2)} veces")
print(f"La letra o frase {letra3} aparece {texto.count(letra3)} veces")
print()

print("Conteo número de palabras en el texto")
lista=texto.split(" ");
print(f"El texto tiene {len(lista)} palabras")
print()

print("Primer letra del texto "+texto[0])
print("Última letra del texto "+texto[-1])
print()

print("Texto con orden invertido mediante slicing utilizando una lista")
lista_invertida=lista[::-1];
new_text=" ".join(lista_invertida)
print(new_text)
print()

print("Verificar si la palabra python se encuentra dentro del texto con condicional if")
resultado= 'python' in texto;
if resultado:
    print("La palabra 'Python' se encuentra incluida en el texto")
else:
    print("La palabra 'Python' no se encuentra incluida en el texto")
print()

print("Verificar si la palabra python se encuentra dentro del texto utilizando operador ternario ")
resultado= True if 'python' in texto else False;
if resultado:
    print("La palabra 'Python' se encuentra incluida en el texto")
else:
    print("La palabra 'Python' no se encuentra incluida en el texto")
print()

print("Verificar si la palabra python se encuentra dentro del texto utilizando un diccionario ")
busqueda='python' in texto;
diccionario={True:"si", False:"no"};
print(f"La palabra 'Python' {diccionario[busqueda]} se encuentra incluida en el texto");
print(diccionario[busqueda]);
print()
