class Vehiculos():

	def __init__(self, marca, modelo):	# Constructor

		# Propiedades
		self.marca=marca
		self.modelo=modelo
		self.en_marcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.en_marcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.en_marcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)

#--------------

class Moto(Vehiculos):	#  Herencia --> clase_hija(clase_padre)
	
	hcaballito=""			# Propiedad propia de la clase Moto

	def caballito(self):	# Método propio de la clase Moto
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):		# Sobreescribe el método de la clase padre
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.en_marcha,
			"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena, "\n",self.hcaballito)

#--------------

class Furgoneta(Vehiculos):	# Hereda de Vehiculos

	def carga(self,cargar):	# pone una carga en la furgoneta e informa 
		self.cargado = cargar
		if (self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"

#--------------

class VElectricos(Vehiculos):

	def __init__(self,marca,modelo):			# Constructor 

		super().__init__(marca,modelo)

		self.autonomia = 100

	def cargar_energia(self):	# Pone a cargar el vehiculo electrico
		self.cargando=True

#--------------

class BicicletaElectrica(VElectricos, Vehiculos):	# Herencia múltiple
	pass

# P.Princial --------------

miMoto = Moto("Suzuki","Samurai")	# Al heredar de vehiculos, hereda su constructor y métodos

miMoto.caballito()	# Método propio de la clase Moto

miMoto.estado()		# Metodo estado de clase Moto que sobreescribe el metodo estado de la clase Vehiculo

miFurgoneta = Furgoneta("Renault","C15")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

miBici = BicicletaElectrica("Orbea","JH1500")	# Hereda de VElectricos() y Vehiculos(marca, modelo) // Toma el constructor de la primera clase por parámetro en la clase

print(miBici.cargar_energia())

