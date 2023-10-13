from pathlib import Path

print("Manejo de archivos utilizando objeto PATH, que es generico para cualquier sistema operativo. En este caso la ruta se escribe con el uso de barras invertidas '/'")
#La ruta puede ser escrita indicando la ubicacion del disco o sin indicar la ubicacion
carpeta = Path('E:/Proyectos_Python/Documentacion/3.Manejo_archivos/alternativa')
#carpeta = Path('/Proyectos_Python/Documentacion/3.Manejo_archivos/alternativa')
#Concatenacion de nombre del archivo y la ruta anterior
archivo = carpeta / 'registro.txt'
mi_archivo=open(archivo)
print(mi_archivo.read())
mi_archivo.close()


######################################
print("\nEliminar líneas de código concatenando directamente sobre el path")
carpeta = Path('/Proyectos_Python/Documentacion/3.Manejo_archivos/alternativa') / 'registro.txt'
mi_archivo=open(archivo)
print(mi_archivo.read())
mi_archivo.close()


print("\nUtilizando with para abrir archivo. El uso del parametro WITH hace que no sea necesario cerrar el archivo ya que lo cierra automaticamente")
# Abre el archivo en modo lectura y guarda el contenido en una variable
with archivo.open('r') as archivo_abierto:
    contenido = archivo_abierto.read()

# Imprime el contenido leído
print(contenido)
