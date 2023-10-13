class Persona:
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

class Cliente(Persona):
    #Inicializo balance en 0 por defecto
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre,apellido)  #Heredo los atributos nombre y apellido de la clase Persona
        self.numero_cuenta=numero_cuenta
        self.balance=balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"

    def depositar(self, monto_deposito):
        self.balance+= monto_deposito
        print("Deposito aceptado.\n")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado con éxito\n")
        else:
            print("Fondos insuficientes\n")

def crear_cliente():
    nombre_cl=input("Ingrese su nombre: ")
    apellido_cl=input("Ingrese su apellido: ")
    numero_cuenta=input("Ingrese su número de cuenta: ")
    cliente=Cliente(nombre_cl,apellido_cl,numero_cuenta)
    return cliente

def inicio():
    mi_cliente=crear_cliente()
    print(mi_cliente)

    opcion=0
    while opcion!='S':
        print('''Elige una opción: 
        * Depositar (D)
        * Retirar (R)
        * Salir (S)
        ''')
        opcion=input()

        if opcion == 'D':
            monto_dep=int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)

        elif opcion == 'R':
            monto_retiro=int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_retiro)

        print(mi_cliente)
        print("Gracias por utilizar el banco de pruebas\n")

inicio()