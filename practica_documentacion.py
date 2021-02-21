class Areas:

	""" Esta clase calcula las areas de diferentes figuras geometricas """

	def areaCuadrado(lado):

		""" Cálcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro """

		return "El área del cuadrado es: " + str(lado*lado)

	def areaTriangulo(base, altura):

		""" Cálcula el área de un triángulo de base y altura pasados por parámetros """

		return "El área del triángulo es: " + str((base*altura)/2)

# print(areaCuadrado(10))

# print(areaCuadrado.__doc__)

# help(areaCuadrado)

help(Areas)