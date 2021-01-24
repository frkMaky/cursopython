
# Sintaxis class NombreClase():
class Coche():

	def __init__(self):	# Constructor de la clase
		# Propiedades de la clase
		self.__largoChasis = 250		# self.NombrePropiedad e inicialización 
		self.__anchoChasis = 120
		self.__ruedas = 4				# self.__propiedad encapsulada
		self.__en_marcha = False

	# Comortamiento de la clase - métodos
	"""
	def function(self):	
		pass
	"""
	def arrancar(self,arrancamos):	# Pone en marcha el coche

		self.__en_marcha = arrancamos

		if (self.__en_marcha):
			chequeo = self.__chequeo_interno()

		if (self.__en_marcha and chequeo):
			return "El coche está en marcha"
		elif (self.__en_marcha and chequeo==False):
			return "Algo ha ido mal en el chequeo, no se puede arrancar"
		else:
			return "El coche está parado"

		#self.en_marcha = True


	def estado(self):	# Devuelve el estado del coche
		print("El coche tiene ",self.__ruedas, " ruedas. Un ancho de ",self.__anchoChasis," y un largo de ", self.__largoChasis)

	def __chequeo_interno(self):	# __nombre_funcion() funcion encapsulada solo accesible desde la propia clase
		print("Realizando chequeo interno...")

		# Iniciamos los pilotos de pruebas
		self.gasolina = "ok"
		self.aceite = "ok"
		self.puertas = "cerradas"

		if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False


#P. Principal

print("Creamos el primer coche -----")

miCoche = Coche()	# Equivalente en otros leguajes a miCoche = new Coche()
# print("Largo del chasis:", miCoche.largoChasis)				# No se puede acceder a propiedades encapsuladas
# print("Ancho del chasis:", miCoche.anchoChasis)
# print("Nº de ruedas:", miCoche.ruedas)
print(miCoche.arrancar(True))									# Se pone en marcha el coche
miCoche.estado()

print("Creamos el segundo coche -----")

miCoche2 = Coche()
# print("Largo del chasis:", miCoche2.largoChasis)
# print("Ancho del chasis:", miCoche2.anchoChasis)

# miCoche2.ruedas =5 	# Se encapsulan las propiedades con self.__propiedad encapsulada

# print("Nº de ruedas:", miCoche2.ruedas)
print(miCoche2.arrancar(False))								# No se arranca el coche
miCoche2.estado()





