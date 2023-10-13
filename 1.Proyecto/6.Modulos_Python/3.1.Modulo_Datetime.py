from datetime import datetime, date

print("Utilizar datetime de import datetime para crear una nueva fecha:")
mi_fecha=datetime(2024,5,10,22,12,43,54)
print(mi_fecha)
print()

print("Cambiar un dato de mi fecha utilizando metodo replace(): ")
mi_fecha=mi_fecha.replace(month= 11)
print(mi_fecha)
print()

print("calcular fechas utilizando Date")
nacimiento = date(1995,3,4)
defuncion=date(2095,5,19)
vida=defuncion -nacimiento
print(vida)  # Retorna numero de dias y horas =>  36601 days, 0:00:00
print(vida.days)
print()

print("Calcular el tiempo que descanso (durmio) una persona utilizando datetime: ")
despierta=datetime(2022,10,5,7,30)
duerme=datetime(2022,10,5,23,45)
vigilia=duerme-despierta
print(vigilia) # En este caso estuvo 16 horas-15 min y 0 segundos => 16:15:0
print(vigilia.seconds) # Número de segundos que descanso =>58500
print()

print("Fecha actual => datetime.now()")
# Obtener la fecha y hora actuales
fecha_actual = datetime.now()
# Imprimir la fecha y hora actuales
print(fecha_actual)
print("Dia actual => date.today()")
# Obtener la fecha actual sin la hora
fecha_solo = date.today()
# Imprimir la fecha actual sin la hora
print(fecha_solo)