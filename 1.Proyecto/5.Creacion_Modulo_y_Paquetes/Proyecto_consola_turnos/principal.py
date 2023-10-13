import numeros

def preguntar():
    print("Bienvenido al centro de atención CARITAS")
    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosméticos\n")
        try:
            mi_rubro = input("Eliga su rubro: ").upper()
            ["P","F","C"].index(mi_rubro)  #Permite verificar la posicion de la letra en la lista si existe
        except ValueError:
            print("Esa no es una opción valida\n")
        else:
            break #Sale del while cuando se ingresa una opción valida

    numeros.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno=input("Quieres sacar otro turno?  [S] [N]\n").upper()
            ["s","N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción valida\n")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()
