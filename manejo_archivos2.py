from io import *	# Directiva para trabajar con archivos

archivo_texto = open("archivoTXT","r+")	# Abrir archivo ("nombre","modo") - r, w, a, r+ (lectura y escritura)

print(archivo_texto.read())	# Se imprime el contenido del archivo
print("-----")

# método seek(indice) para poner el puntero del archivo en la posición indicada

archivo_texto.seek(5)

print(archivo_texto.read())	# Se imprime el contenido del archivo desde la posición del puntero
print("-----")

archivo_texto.seek(0)	# Puntero al principio

print(archivo_texto.read(11))	# Se lee archivo hasta el indice indicado
print("-----")

archivo_texto.seek(len(archivo_texto.read())/2)	# Puntero justo al medio

print(archivo_texto.read()) # Se imprime la mitad final
print("-----")

archivo_texto.seek(0)	# Puntero al principio
archivo_texto.seek(len(archivo_texto.readline()))	# Puntero justo al final de la primera linea
print(archivo_texto.read()) # Se imprime sin la primera linea
print("-----")

archivo_texto.seek(0)	# Puntero al principio
lista_texto = archivo_texto.readlines()	# Se guarda lista
lista_texto[1] = "Esta linea ha sido incluida desde el exterior\n"
archivo_texto.writelines(lista_texto)	# Se escribe el contenido en el archivo
archivo_texto.seek(0)
print(archivo_texto.read())

archivo_texto.close()
