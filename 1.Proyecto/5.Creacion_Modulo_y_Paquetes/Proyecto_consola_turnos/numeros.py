def numeros_perfumeria():
    for n in range(1,1000):
        yield f"P - {n}"

def numeros_farmacia():
    for n in range(1,1000):
        yield f"F - {n}"

def numeros_cosmetico():
    for n in range(1,1000):
        yield f"C - {n}"


perfumeria=numeros_perfumeria()
farmacia=numeros_farmacia()
cosmeticos=numeros_cosmetico()

def decorador(rubro):
    print("\n"+"*"*23)
    print("Su número es: ")
    if rubro == 'P':
        print(next(perfumeria))
    elif rubro=='F':
        print(next(farmacia))
    else:
        print(next(cosmeticos))
    print("Aguarde su turno para ser atendido")
    print("*"*23+"\n")