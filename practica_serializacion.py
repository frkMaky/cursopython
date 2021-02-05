import pickle	# Biblioteca para serializar (binario)

# Guardar fichero en binario ----------------------------

lista_nombres = ["Pedro","Ana","María","Isabel"]

fichero_binario = open("listaNombres","wb")	# Modo escritura binario wb

pickle.dump(lista_nombres, fichero_binario)	# Se vuelca la lista nombres en el fichero binario

fichero_binario.close()	# Se cierra fichero

# Recuperar fichero en binario ----------------------------

fichero2 = open("listaNombres","rb")	# Modo lectura binario rb

lista = pickle.load(fichero2)	# Se carga la información de fichero2 en lista

print(lista)

fichero2.close()

