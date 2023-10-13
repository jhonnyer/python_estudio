from mis_paquetes import suma_resta
from mis_paquetes.subpaquete import saludo

print("\nUtilizar el paquete e importar módulo suma_resta.py => 'from mis_paquetes import suma_resta'")
print("'suma_resta.resta(15,2)'")
print("'suma_resta.suma(15,2)'\n")

suma_resta.resta(15,2)
suma_resta.suma(7,4)
print()

###############################################
## Utilización subpaquete
###############################################

print("\nUtilizar un subpaquete e importar el método saludo().  => 'from mis_paquetes.subpaquete import saludo'")
print("'saludo.saludo()'\n")
saludo.saludo()
print()



