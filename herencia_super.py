class Persona():
	
	def __init__(self,nombre,edad,residencia): 
		self.nombre = nombre
		self.edad = edad
		self.residencia = residencia

	def descripcion(self):
		print("Nombre: ",self.nombre," Edad: ",self.edad," Lugar de residencia: ",self.residencia)

class Empleado(Persona):

	def __init__(self, salario, antigüedad, nombreEmpleado,edadEmpleado,residenciaEmpleado):

		super().__init__(nombreEmpleado,edadEmpleado,residenciaEmpleado)	# LLama a constructor de la clase padre -> super()

		self.salario = salario
		self.antigüedad = antigüedad

	def descripcion(self):

		super().descripcion() # LLama a descripcion de la clase padre -> super()

		print("El empleado tiene un salario de ",self.salario," y una antigüedad de ", self.antigüedad)


#------------------------------------------------------

Antonio = Empleado(1500, 15,"Antonio", 35, "Vigo" )

Antonio.descripcion()

print(isinstance(Antonio,Empleado))	# True si la instancia pertenece a la Clase

print(isinstance(Antonio,Persona))	# True si la instancia pertenece a la Clase (Empleado al heredar de Pesona True)

Manuel = Persona("Manuel",25,"Jaén")

print(isinstance(Manuel,Empleado))	# True si la instancia pertenece a la Clase Empleado (False, al se de la clase Persona)