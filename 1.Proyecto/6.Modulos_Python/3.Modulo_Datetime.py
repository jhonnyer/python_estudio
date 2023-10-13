'''
El módulo datetime (incorporado en Python) puede importarse en proyectos para trabajar con fechas y horas, así como intervalos y duraciones.

import datetime
mi_fecha = datetime.date(año,mes,día)

año,mes,día son integers comprendidos en los rangos de fechas "reales" (12 meses y 31 días como máximo). También podemos extraer el año, mes y día individualmente

anio = mi_fecha.year
mes = mi_fecha.month
dia = mi_fecha.day

Obtener el día actual => hoy = datetime.date.today()

mi_hora = datetime.time(hora, minuto, segundo, microsegundo)

Todos los argumentos son opcionales (se asumen 0 si no se indican), y deben estar comprendidos entre 0 y 24 para las horas, 0 y 60 para minutos y segundos, y 0 y 1000000 para los microsegundos.

fecha_hora = datetime.datetime(año, mes, día, hora, minuto, segundo, microseg)

Obtener fecha y hora actual => ahora = datetime.datetime.now()

Obtener horas, minutos y segundos:
hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second
'''
import datetime

print("Creación de hora, los valores que no se indiquen se llenan en cero. Formato => Hora:Minutos:segundos:microsegundos")
mi_hora=datetime.time(16,35)
print(mi_hora)
mi_hora=datetime.time(16,35,54,15)
print(mi_hora)
print(mi_hora.minute)
print()


print("Creación de dia, formato => Año-Mes-Dia, se deben ingresar todos los datos")
mi_dia=datetime.date(2025,10,18)
print(mi_dia)
print("\nPuedo obtener los datos independientes de año, dia y mes de la variable mi dia creada anteriormente:")

print(mi_dia.year)
print(mi_dia.month)
print(mi_dia.day)
print("\nFormato de fecha ctime() => Dia, Mes, Hora, Año")
print(mi_dia.ctime())
print()

print("\nVerificar dia actual con metodo today(), la variable donde se ejecuta sea de tipo Date")
print(mi_dia.today())
print()


print("Fecha nueva a partir de la fecha actual => datetime.datetime.now()")
# Obtener la fecha y hora actuales
fecha_actual = datetime.datetime.now()
# Imprimir la fecha y hora actuales
print(fecha_actual)
print()

print("Dia actual")
hoy=datetime.datetime.today()
print(hoy)
anio=hoy.year
print(anio)