#En Python 3.10, se incorpora la coincidencia de patrones estructurales mediante las declaraciones match y case. Esto permite asociar acciones específicas basadas en las formas o patrones de tipos de datos complejos.
#Match significa coincidencia, similar al switch case de otros lenguales, pero mas avanzado, tiene funciones superiores
print("Arreglo condiciones normal con if")
serie="N-02"
if serie == "N-01":
    print("Samsung")
if serie == "N-02":
    print("Nokia")
if serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")
print()

#############################
print("Arreglo condiciones con MATCH")
serie="N-02"
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")
print()


#############################
print("Ejemplo funciones avanzadas MATCH, verificando estructura de datos\n")
cliente ={
    'nombre':'Jhonnyer',
    'edad':45,
    'ocupacion':'Desarrollador'
}

pelicula={
    'titulo':'Matrix',
    'ficha_tecnica':{
        'protagonista':'Keanu reeves',
        'director':'Lana y Lilly Wachowsky'
    }
}

elementos = [cliente, pelicula, 'libro']

#Vamos a buscar coincidencias
for e in elementos:
    match e:
        #Verificamos la estructura del elemento
        case {
            'nombre': nombre,
            'edad': edad,
            'ocupacion': ocupacion
        }:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
            print()
        case {
            'titulo':titulo,
            'ficha_tecnica': {
                'protagonista': protagonista,
                'director': director
            }
        }:
            print("Es una pelicula")
            print(titulo, protagonista, director)
            print()
        case _:
            print("\nNo tiene relacion")

print()