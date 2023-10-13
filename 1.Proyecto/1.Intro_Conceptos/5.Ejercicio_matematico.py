
nombre=input("Digita tu nombre: ")
venta_total=0;
venta_parcial=int(input("Digita el valor de la venta: "));
venta_total=venta_total+venta_parcial
venta_parcial=int(input("Digita el valor de la venta: "));
venta_total=venta_total+venta_parcial
print(f"{nombre} tuvo un valor de la venta total de: {venta_total}, y la comisión de la venta es de: {round((venta_total*13)/100,2)}");