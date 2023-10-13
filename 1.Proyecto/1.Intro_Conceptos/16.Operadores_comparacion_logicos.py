#Operadores de comparacion, son operadores lógicos que permite verificar si una condicion es verdadera o False
#   >    Mayor que
#   <    Menor que
#   >=   Mayor o igual que
#   <=   Menos o igual que
#   ==   Igual que
#   !=   Diferente que

res1=10==25
print(res1)
print()

res2=5+5 == 18-8
print(res2)
print()

#Comparacion de string
print("Comparacion entre string, en este caso el programa reconoce o es sensible entre mayusculas y minusculas")
texto_result1= 'blanco'=='blanco';
texto_result2= 'blanco'=='Blanco';
texto_result3= 'blanco'=='Blanco'.lower();
texto_result4= '100'==100;
texto_result5=  100.0==100;
print(f"Resultado comparacion 'blanco'=='blanco' es: {texto_result1}");
print(f"Resultado comparacion 'blanco'=='Blanco' es: {texto_result2}");
print(f"Resultado comparacion 'blanco'=='Blanco'.lower() es: {texto_result3}");
print(f"Resultado comparacion entre un string y un entero '100'==100 es: {texto_result4}");
print(f"Resultado comparacion entre un flotante y un entero 100.0==100 es: {texto_result5}");
print()

print(f"Diferente que 5!=3 {5!=3}");
print(f"Mayor que 5>3 {5>3}");
print(f"Menor que 5<3 {5<3}");