import pickle	# Biblioteca para serializar (binario)

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

#------

coche1 = Vehiculos("Seat","Panda")
coche2 = Vehiculos("Audio","A4")
coche3 = Vehiculos("Renault","Clio")

coches =[coche1,coche2,coche3]	# Se crea una coleccion de coches

fichero = open("Los Coches","wb")	# se abre el fichero escritura de bytes

pickle.dump(coches,fichero)		# Se vuelca coleccion en fichero
	
fichero.close()	# Se cierra fichero

# Lectura del fichero ------------

ficheroLectura = open("Los Coches","rb") # se abre el fichero lectura de bytes

misCoches = pickle.load(ficheroLectura) # Se vuelca fichero en variable

ficheroLectura.close() # Se cierra fichero

for coche in misCoches:
	coche.estado()
	print("-----")