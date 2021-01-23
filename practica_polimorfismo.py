class Coche():

	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")

class Moto():

	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")

class Camion():

	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")

#----- # Polimorfismo - El comportamiento del mismo método varia en función de la clase a la que pertenece

def desplazamientoVehiculo(vehiculo):
	# LLama al método desplazamiento del vehiculo
	vehiculo.desplazamiento()

#-----

miVehiculo = Moto()

miVehiculo.desplazamiento()		

miVehiculo2 = Coche()

miVehiculo2.desplazamiento()

miVehiculo3 = Camion()

desplazamientoVehiculo(miVehiculo3)	# Polimorfismo - 