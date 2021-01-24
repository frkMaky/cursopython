from io import *	# Directiva para trabajar con archivos

# Modo escritura ------------------------------

archivo_texto = open("archivoTXT","w")	# Abrir archivo ("nombre","modo") - r, w, a, r+ (lectura y escritura)

frase ="Estupendo día para trabajar con archivos\ny seguir aprenfiendo Python"

archivo_texto.write(frase) 	# Se escribe en el archivo

print("Se ha creado el archivo y añadido la frase, comprueba el directorio")

archivo_texto.close()	# Se cierra el archivo

# Modo agrgar informacion ------------------------------

archivo_texto = open("archivoTXT","a")	# Abrir archivo ("nombre","modo") 

archivo_texto.write("\nSiempre es una buena ocasión para agregar texto")	# Se añade contenido al archivo

archivo_texto.close()	# Se cierra el archivo

# Modo lectura ------------------------------

archivo_texto = open("archivoTXT","r")	# Abrir archivo ("nombre","modo") 

# texto = archivo_texto.read() # Se guarda el contenido del archivo en una variable

# print(texto)	# Se imprime el contenido del archivo

lineas_texto = archivo_texto.readlines()	# Se guarda el archivo en formato de lista

for linea in lineas_texto:	# Se imprime contenido linea a lineas
	print(linea)

archivo_texto.close()	# Se cierra el archivo
