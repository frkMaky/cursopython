# Función tradicional

def generaPares(limite):
	# Función que genera nº pares
	num=1							#contador
	miLista=[]						#lista vacia de numeros generados
	while num<limite:				#mientras no se llega al limite
		miLista.append(num*2)		#se añade un nº par a la lista
		num+=1						#y se pasa al siguiente
	return miLista					#Al terminar se devuelve la lista

print(generaPares(10))


# Con un generador	(MAS EFICIENTE)

def generaPares2(limite):
	# Función que genera nº pares
	num=1							#contador
	while num<limite:				#mientras no se llega al limite
		yield num*2					# SE DEVUELVE el doble del num (nº par)
		num+=1						#y se pasa al siguiente
	
devuelve_pares = generaPares2(10)	# Objeto iterable que devuelve la función

"""
for i in devuelve_pares:			# Se recorre el objeto devuelto
	print(i)						# Imprimiendo cada valor
"""
# next(objeto_iterable) -> Acceder al siguiente  elemento devuelto por yield (generador)

print(next(devuelve_pares))			# Se devuelve el siguiente valor del objeto iterable
print("Aqui podrí ir más código")	# No se tiene que recorrer todo el objeto, se accede elemento a elemento

print(next(devuelve_pares))			# Se devuelve el siguiente valor del objeto iterable
print("Aqui podrí ir más código")	# No se tiene que recorrer todo el objeto, se accede elemento a elemento

print(next(devuelve_pares))			# Se devuelve el siguiente valor del objeto iterable
print("Aqui podrí ir más código")	# No se tiene que recorrer todo el objeto, se accede elemento a elemento