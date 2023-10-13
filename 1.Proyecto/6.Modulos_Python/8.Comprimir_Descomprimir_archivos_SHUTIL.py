import shutil

print("Comprimir archivo usando shutil")
carpeta_origen='E:\\Proyectos_Python\\Documentacion\\6.Modulos_Python'
archivo_destino='Todo_Comprimido'
shutil.make_archive(archivo_destino,'zip',carpeta_origen)
print()

print("Descomprimir archivo usando shutil  =>  shutil.unpack_archive('Todo_Comprimido.zip','Extraccion_terminada','zip')")
print("'Extraccion_terminada' es el nombre de la carpeta donde va a quedar los archivos descomprimidos de tipo zip")
shutil.unpack_archive('Todo_Comprimido.zip','Extraccion_terminada','zip')

