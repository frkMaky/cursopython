
"""
yield from para simplificar bucles for anidados
"""

def devuelve_ciudades(*ciudades):	# 	(* -> nº indeterminado de argumentos | ciudades -> recibidos en forma de Tupla)
	# Función generador
	for elemento in ciudades:			# Se accede a cada ciudad pasada
		"""
		for subElemento in elemento:	# Se accede a cada letra de la ciudad
			yield subElemento			# Se devuelve la siguiente letra
		"""
		yield from elemento 			# yield from evita tener que utilizar for anidados 

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Vigo","Valencia")	# Se genera objeto iterador de la función generador

# Se muestran los elementos del objeto iterador / Letra a letra de cada ciudad

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))