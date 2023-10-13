'''boton.pack(fill=X) =>  La línea de código boton.pack(fill=X) aplicada a un botón (boton) en un entorno de interfaz gráfica (GUI) utilizando la biblioteca tkinter de Python hará que el botón se expanda horizontalmente para llenar todo el espacio disponible en el contenedor padre en la dirección horizontal (a lo largo del eje X).'''

#TKinter => Permite generar una interfaz grafica de usuario
#Colores pantalla Tkinter
#https://es.wikibooks.org/wiki/Python/Interfaz_gr%C3%A1fica_con_Tkinter/Los_nombres_de_los_colores
from tkinter import *
import random #Para generar recibos aleatorios
import datetime
from tkinter import filedialog, messagebox  #Para exportar los archivos de los recibos

#Botones de la calculadora presionados
operador=''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]
def click_boton(numero):
    global operador
    operador=operador+numero
    #muestra lo que se haya presionado en la calculadora
    #visor_calculadora.insert(END,operador)
    visor_calculadora.delete(0, END)  # Borra el contenido anterior
    visor_calculadora.insert(END, operador)  # Inserta el nuevo contenido

#Funcion borrar()
def borrar():
    global operador
    operador=''
    visor_calculadora.delete(0,END)

#Funcion obtener resultado
def obtener_resultado():
    global operador
    resultado=str(eval(operador))  #EValua la operacion
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador=''

def revisar_check():
    #REVISAR COMIDAS
    x=0
    for c in cuadros_comida:
        if variables_comida[x].get()==1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get()=='0':
                cuadros_comida[x].delete(0,END) #Cada que se activa un revisar check se bnorra el cero
            cuadros_comida[x].focus() #Permite observar un cursor en el cuadro del check
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x+=1

    # REVISAR BEBIDAS
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)  # Cada que se activa un revisar check se bnorra el cero
            cuadros_bebida[x].focus()  # Permite observar un cursor en el cuadro del check
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    # REVISAR POSTRES
    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)  # Cada que se activa un revisar check se bnorra el cero
            cuadros_postre[x].focus()  # Permite observar un cursor en el cuadro del check
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1


#Funcion total sumar cantidad del pedido
def total():
    #Precios Comida
    sub_total_comida=0
    p=0
    for cantidad in texto_comida:
        sub_total_comida=sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p+=1

    # Precios Bebida
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    # Precios Postres
    sub_total_postres = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total=sub_total_comida+sub_total_postres+sub_total_bebida
    impuestos=sub_total*0.07
    total=sub_total+impuestos

    #Establecer los contenidos a las variables visualizadas en la GUI.
    var_costo_comida.set(f"$ {round(sub_total_comida,2)}")
    var_costo_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    var_costo_postre.set(f"$ {round(sub_total_postres, 2)}")
    var_subtotal.set(f"$ {round(sub_total, 2)}")
    var_impuestos.set(f"$ {round(impuestos, 2)}")
    var_total.set(f"$ {round(total, 2)}")

def recibo():
   texto_recibo.delete(1.0, END)
   num_recibo=f'N# - {random.randint(1000,9999)}'
   fecha=datetime.datetime.now()
   fecha_recibo=f'{fecha.day}/{fecha.month}/{fecha.year}-{fecha.hour}:{fecha.minute}'
   texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')

   texto_recibo.insert(END,f'*'*47+'\n')
   texto_recibo.insert(END,'Items\t\tCant.\tCosto tems\n')
   texto_recibo.insert(END,f'-'*54+'\n')

   x=0
   for comida in texto_comida:
       if comida.get()!='0':
           texto_recibo.insert(END,f'{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get())*precios_comida[x]}\n')
       x+=1

   x = 0
   for bebida in texto_bebida:
       if bebida.get() != '0':
           texto_recibo.insert(END,
                               f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n')
       x += 1

   x = 0
   for postre in texto_postre:
       if postre.get() != '0':
           texto_recibo.insert(END,
                               f'{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postres[x]}\n')
       x += 1

   texto_recibo.insert(END, f'-' * 54 + '\n')
   texto_recibo.insert(END,f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
   texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
   texto_recibo.insert(END, f' Costo de los Postres : \t\t\t{var_costo_postre.get()}\n')
   texto_recibo.insert(END, f'-' * 54 + '\n')
   texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
   texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuestos.get()}\n')
   texto_recibo.insert(END, f' Total : \t\t\t{var_total.get()}\n')
   texto_recibo.insert(END, f'*' * 47 + '\n')
   texto_recibo.insert(END, ' Los esperamos pronto')

#Funcion para guardar factura e imprimir recibo
def guardar():
    info_recibo=texto_recibo.get(1.0,END) #Pasamos a la variable info_recibo todo lo que tiene actualmente el recibo
    archivo=filedialog.asksaveasfile(mode='w',defaultextension='.txt') #Creamos un archivo de tipo texto con propiedad de escritura
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información','Su recibo ha sido guardado')  #mensaje cuando el archivo ha sido guardado

def resetear():
    texto_recibo.delete(0.1,END) #Borramos desde el comienzo hasta el final

    #Borrar el texto que hay en los checbkox
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    #Deshabilitar los checkbox despues de resetear valores
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    #Quitar seleccion de los checkbox
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    #Resetear valores variables
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')

#Iniciar tkinter
aplicacion =Tk()

#Tamaño de la ventana
aplicacion.geometry('1196x630+0+0') #Tamaño alto(630) y ancho(1020), +0 (posicion ubicacion pantalla eje x) +0 (posicion ubicacion pantalla eje y)

#Que la pantalla no se pueda maximizar
aplicacion.resizable(0,0)

#Titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturación")

#Color de fondo de la ventana
aplicacion.config(bg='burlywood')

#Panel superior => bd hace referencia ancho del bordo, relief tipo de relieve
panel_superior=Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)  #Ubicar el panel superior en la parte de arriba(superior)

#Etiqueta del titulo, text= Titulo facturacion, fg color de las letras, font indica tipo fuente letra, width ancho de la etiqueta
etiqueta_titulo=Label(panel_superior, text="Sistema de Facturación",fg='azure4', font=('Dosis',49),bg='burlywood',width=26)

etiqueta_titulo.grid(row=0,column=0) #Genera una cuadricula

#Panel izquierdo
panel_izquierdo=Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#Panel costos
panel_costos=Frame(panel_izquierdo,bd=1,relief=FLAT, bg='azure4',padx=55)
panel_costos.pack(side=BOTTOM)

#Panel comidas
panel_comidas=LabelFrame(panel_izquierdo, text='Comida',font=('Dosis',19,'bold'),bd=1,relief=FLAT,fg='azure4')
panel_comidas.pack(side=LEFT)

#Panel bebidas
panel_bebidas=LabelFrame(panel_izquierdo, text='Bebidas',font=('Dosis',19,'bold'),bd=1,relief=FLAT,fg='azure4')
panel_bebidas.pack(side=LEFT)

#Panel postres
panel_postres=LabelFrame(panel_izquierdo, text='Postres',font=('Dosis',19,'bold'),bd=1,relief=FLAT,fg='azure4')
panel_postres.pack(side=LEFT)

#Panel derecha
panel_derecha=Frame(aplicacion, bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel calculadora
panel_calculadora=Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood',padx=0, pady=0)
panel_calculadora.pack() #Por defecto si no se pone nada dentro del pach se coloca en la parte superior

#Panel recibo
panel_recibo=Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_recibo.pack() #Por defecto si no se pone nada dentro del pach se coloca en la parte superior

#Panel botones
panel_botones=Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_botones.pack() #Por defecto si no se pone nada dentro del pach se coloca en la parte superior

#Lista de productos
lista_comidas=['pollo','cordero','salmon','merluza','kebab','pizza1','pizza2','pizza3']
lista_bebidas=['agua','soda','jugo','cola','vino1','vino2','cerveza1','cerveza2']
lista_postres=['helado','fruta','brownies','flan','mousse','pastel1','pastel2','pastel3']

#Generar items comida
variables_comida=[]
cuadros_comida=[]
texto_comida=[]
contador=0
for comida in lista_comidas:

    #Crear Checkbutton
    variables_comida.append('')
    variables_comida[contador]=IntVar() #En cada uno de sus indices se va a generar una variable de tipo integer
    comida=Checkbutton(panel_comidas,
                       text=comida.title(),
                       font=('Dosis',19,'bold'),
                       onvalue=1, #onvalue=1 cuando este activo ,offvalue=0 cuando este inactivo
                       offvalue=0,
                       variable=variables_comida[contador],
                       command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W) # stycky=W para que se ubique al lado izquierdo de nuestro panel

    #Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador]=StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador]=Entry(panel_comidas,
                                   font=('Dosis',18,'bold'),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador+=1


#Generar items bebidas
variables_bebida=[]
cuadros_bebida=[]
texto_bebida=[]
contador=0
for bebida in lista_bebidas:

    # Crear Checkbutton
    variables_bebida.append('')
    variables_bebida[contador]=IntVar() #En cada uno de sus indices se va a generar una variable de tipo integer
    bebida=Checkbutton(panel_bebidas,
                       text=bebida.title(),
                       font=('Dosis',19,'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=variables_bebida[contador],
                       command=revisar_check) #onvalue=1 cuando este activo ,offvalue=0 cuando este inactivo
    bebida.grid(row=contador,
                column=0,
                sticky=W) # stycky=W para que se ubique al lado izquierdo de nuestro panel

    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador+=1


#Generar items postres
variables_postre=[]
cuadros_postre=[]
texto_postre=[]
contador=0
for postre in lista_postres:

    # Crear Checkbutton
    variables_postre.append('')
    variables_postre[contador]=IntVar() #En cada uno de sus indices se va a generar una variable de tipo integer
    postre=Checkbutton(panel_postres,
                       text=postre.title(),
                       font=('Dosis',19,'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=variables_postre[contador],
                       command=revisar_check) #onvalue=1 cuando este activo ,offvalue=0 cuando este inactivo
    postre.grid(row=contador,
                column=0,
                sticky=W) # stycky=W para que se ubique al lado izquierdo de nuestro panel

    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)

    contador+=1

#Variables
var_costo_comida=StringVar()
var_costo_bebida=StringVar()
var_costo_postre=StringVar()
var_subtotal=StringVar()
var_impuestos=StringVar()
var_total=StringVar()

#Etiquetas de costo y campos de entrada para comidas
etiqueta_costo_comida=Label(panel_costos,
                            text='Costo Comidas',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida=Entry(panel_costos,
                         font=('Dosis',12,'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1,padx=41)


#Etiquetas de costo y campos de entrada para bebidas
etiqueta_costo_bebida=Label(panel_costos,
                            text='Costo Bebida',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida=Entry(panel_costos,
                         font=('Dosis',12,'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1,padx=41)


#Etiquetas de costo y campos de entrada para postres
etiqueta_costo_postre=Label(panel_costos,
                            text='Costo Postres',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre=Entry(panel_costos,
                         font=('Dosis',12,'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=var_costo_postre)
texto_costo_postre.grid(row=2,column=1,padx=41)


#Etiquetas de costo y campos subtotal
etiqueta_subtotal=Label(panel_costos,
                            text='Subtotal',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal=Entry(panel_costos,
                         font=('Dosis',12,'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3,padx=41)


#Etiquetas de costo y campos impuestos
etiqueta_impuestos=Label(panel_costos,
                            text='Impuestos',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_impuestos.grid(row=1,column=2)

texto_impuestos=Entry(panel_costos,
                         font=('Dosis',12,'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=var_impuestos)
texto_impuestos.grid(row=1,column=3,padx=41)

#Etiquetas de costo y campos total
etiqueta_total=Label(panel_costos,
                            text='Total',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_total.grid(row=2,column=2)

texto_total=Entry(panel_costos,
                         font=('Dosis',12,'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=var_total)
texto_total.grid(row=2,column=3,padx=41)


#BOTONES
botones=['total','recibo','guardar','resetear']
botones_creados=[]
columnas=0
for boton in botones:
    boton=Button(panel_botones,
                 text=boton.title(),
                 font=('Dosis',16,'bold'),
                 fg='white',
                 bg='azure4',
                 bd=1,
                 width=9)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas+=1

#Para los botones creados le pasamos el metodo correspondiente
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

#AREA DE RECIBOS
texto_recibo=Text(panel_recibo,
                  font=('Dosis',14,'bold'),
                  bd=1,
                  width=48,
                  height=10)
texto_recibo.grid(row=0,
                  column=0)

#Calculadora
visor_calculadora=Entry(panel_calculadora,
                        font=('Dosis', 16, 'bold'),
                        bd=1,
                        width=42)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora=['7','8','9','+','4','5','6','-','1','2','3','*','R','B','0','/']
botones_guardados=[]
print(botones_guardados)

fila=1
columna=0
for boton in botones_calculadora:
    boton=Button(panel_calculadora,
                  text=boton.title(),
                  font=('Dosis', 14, 'bold'),
                  #font=('Dosis'),
                  fg='white',
                  bg='azure4',
                  bd=1,
                  width=9,
                  padx=0,
                  pady=0)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)

    #Logica para que solose tengan 4 columnas, cuando pase esto se aumenta la fila y nos permite crear la calculadora de 4 columbas y 4 filas en este caso
    if columna==3:
        fila+=1
    columna+=1

    if columna==4:
        columna=0


#Opciones botones de calcuradora
for i, boton_texto in zip(range(0,16), botones_calculadora):
    if boton_texto=='B':
        botones_guardados[i].config(command=borrar)
    elif boton_texto=='R':
        botones_guardados[i].config(command=obtener_resultado)
    else:
        botones_guardados[i].config(command=lambda text=boton_texto: click_boton(text))


#Evitar que la pantalla se cierre
aplicacion.mainloop()