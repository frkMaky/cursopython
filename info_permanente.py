import pickle

class Persona():

	def __init__(self,nombre,genero,edad):	# Constructor -----
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Nueva persona: ",self.nombre)

	def __str__(self):
		return "> {}  {}  {} <".format(self.nombre,self.genero,self.edad)
#-------------------
class ListaPersonas():

	personas =[]	# lista de personas

	def __init__(self):	# Constructor

		lista_de_personas = open("fichero_exteno","ab+")	# modo agregar binario

		lista_de_personas.seek(0)	# Se pone puntero al principio

		try:
			self.personas = pickle.load(lista_de_personas)
			print ("Se cargaron {} personas".format(len(self.personas)))
		except:
			print("El fichero está vacío")
		finally:
			lista_de_personas.close()
			del(lista_de_personas)

	def agregar_personas(self, p):	# Se añade la persona p a la lista de personas
		self.personas.append(p)
		self.guardar_en_fichero_externo()

	def mostrar_personas(self):
		for p in self.personas:
			print("Persona: ", p)
		self.mostrar_info_fichero_externo()

	def guardar_en_fichero_externo(self):
		lista_de_personas=open("fichero_exteno","wb")
		pickle.dump(self.personas,lista_de_personas)
		lista_de_personas.close
		del(lista_de_personas)
	def mostrar_info_fichero_externo(self):
		print("La información del fichero externo es:")
		for p in self.personas:
			print(p)

#-------------------

lista = ListaPersonas()

p = Persona("Sandra", "Femenino", 29)

lista.agregar_personas(p)

lista.agregar_personas(Persona("Antonio","Masculino",39))

lista.agregar_personas(Persona("Ana","Femenino",19))

lista.mostrar_personas()

print(str(p))
