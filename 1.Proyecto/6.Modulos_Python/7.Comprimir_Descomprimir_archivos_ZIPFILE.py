'''
El formato zip permite comprimir archivos sin pérdida de información, ahorrando espacio de almacenamiento y
manteniendo documentos relacionados en un mismo archivo .zip; utilizando el módulo zipfile:

import zipfile
mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w') => donde:
    archivo_comprimido.zip => nombre archivo a comprimir
    w => permiso de escritura en el archivo zip.

'''
import zipfile
print("Crear archivo comprimido                         =>     mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')")
mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')
print("Almacenar archivos, en mi archivo comprimido     =>      mi_zip.write('9.mi_texto_B.txt')")
mi_zip.write('8.mi_texto_A.txt')
mi_zip.write('9.mi_texto_B.txt')
mi_zip.close()
print()

print("Abrir archivo")
zip_abierto=zipfile.ZipFile('archivo_comprimido.zip','r')
print("Extraer archivo por archivo   =>  zip_abierto.extract('8.mi_texto_A.txt')")
zip_abierto.extract('8.mi_texto_A.txt')
print("Extraer todos los archivos    =>  zip_abierto.extractall()")
zip_abierto.extractall()