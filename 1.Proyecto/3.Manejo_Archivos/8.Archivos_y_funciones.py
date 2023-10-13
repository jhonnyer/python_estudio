'''
Recordatorio: puedes crear funciones para que ejecuten código cada vez que sean invocadas, evitando repeticiones y
facilitando su lectura. Esto aplica para todo Python, y desde luego también cuando manipulamos archivos.
'''

def procesar_archivos(archivo):
    mi_archivo=open(archivo)
    resultado=mi_archivo.read()
    mi_archivo.close()
    return resultado

def sobrescribir(archivo):
    mi_archivo=open(archivo,'w')
    mi_archivo.writelines("contenido eliminado")
    mi_archivo.close()

def registro_error(archivo):
    mi_archivo=open(archivo,'a')
    mi_archivo.writelines("\nse ha registrado un error de ejecución")
    mi_archivo.close()

archivo = r'E:\Proyectos_Python\Documentacion\3.Manejo_archivos\prueba_funciones.txt'
sobrescribir(archivo)
registro_error(archivo)
resultado=procesar_archivos(archivo)
print(resultado)
