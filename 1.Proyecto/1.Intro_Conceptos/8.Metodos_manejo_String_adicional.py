#Nota: Existen mas de 30 metodos pero estos son los más comunes.

texto=" Esto es UN Texto de Pruebas";
#Upper pasar a mayusculas
resultado =texto.upper();
print(resultado);

#Si queremos obtener solo un caracter del texto en mayuscula, en este caso el indice 2.
print(texto[2].upper());

#lower pasar a minusculas
print(texto.lower());

#split separar el texto en partes y convertir en una lista
resultado=texto.split();
print(resultado);

#Añadir un separador para la lista, en este caso la letra t.
print(texto.split("t"));

#join unir items usando un separador especifico, en el ejemplo se unen las variables a,b, c y d mediante un separador de espacio "".
a="Aprender";
b="Python";
c="es";
d="genial";
e=" ".join([a,b,c,d]);
print(e);

lista_palabras = ["La","legibilidad","cuenta."]
a=" ".join(lista_palabras);
print(a);

#find encontrar un sub-string - Con find si se busca un caracter que no existe, retorna -1 mientras que index retorna un error
print(texto.find("s"));
print(texto.find("Pruebas"));
print(texto.find("z"));

#replace es utilizado para  reemplazar un substring, en este caso la palabra Pruebas por verificación en el texto original.
resultado=texto.replace("Pruebas","verificación");
print(resultado);


texto="Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado=texto.replace("difícil","fácil");
resultado=resultado.replace("mala","buena");
print(resultado);

texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
reemplazos = {
    "difícil": "fácil",
    "mala": "buena"
}
print(reemplazos.items());

resultado = texto
for palabra_original, palabra_reemplazo in reemplazos.items():
    resultado = resultado.replace(palabra_original, palabra_reemplazo)

print(resultado)
