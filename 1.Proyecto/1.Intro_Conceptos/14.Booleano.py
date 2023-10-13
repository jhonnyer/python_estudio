#Un elemento booleano solo puede tener dos valores True o False
#los booleanos pueden ser utilizados para evaluar una condicion si es verdadera o falsa por ejemplo 5<3.
#Operaciones con Booleanos

#   >    Mayor que
#   <    Menor que
#   >=   Mayor o igual que
#   <=   Menos o igual que
#   ==   Igual que
#   !=   Diferente que
#   mi_bool = 5 in mi_lista;
#   mi_bool = 5 not in mi_lista;

var1=True  #Los valores True o False deben empezar la primer letra con mayuscula como aparece en el ejemplo
var2=False
print(type(var1))
print(var1)
print(var2)
print()

print("Asignacion de un booleano mediante una comparacion logica de mayor que")
numero= 5 > 2+3
print(type(numero))
print(numero)
print()

print("Asignacion de un booleano mediante una comparacion logica de igualdad")
numero= 5 == 2+3
print(type(numero))
print(numero)
print()

print("Asignacion de un booleano mediante una comparacion logica diferente que")
numero= 5 != 2+3
print(type(numero))
print(numero)
print()

print("Asignacion de un booleano utilizando el metodo bool() para una comparacion logica ")
numero= bool(5 <= 2+3)
print(type(numero))
print(numero)
print()

print("Asignacion de un booleano de valor Falso")
numero= bool()
print(type(numero))
print(numero)
print()

print("Verificar si un valor se encuentra en una lista")
lista= [1,2,3,4]
control1= 5 in lista
control2= 5 not in lista
print("Verificacion si 5 se encuentra en la lista")
print(type(control1))
print(control1)
print("Verificacion si 5 no se encuentra en la lista")
print(type(control2))
print(control2)
print()

print("Operacion matematica comparacion (17834/34) > (87*56)")
resultado=(17834/34) > (87*56)
print(resultado);

print("Resultado comparacion print(5 == 25**0.5);")
print(5 == 25**0.5);