class Empleado:

	def __init__(self,nombre,cargo,salario):
		self.nombre =nombre 
		self.cargo =cargo 
		self.salario =salario

	def __str__(self):
		return "{} que trabaja como {} y tiene un salario de {}".format(self.nombre,self.cargo,self.salario)

listaEmpleados =[
Empleado("Juan","Director",6700),
Empleado("Ana","Presidenta",7500),
Empleado("Antonio","Administrativo",2100),
Empleado("Sara","Secretaria",2150),
Empleado("Mario","Botones",1800),
]

def calculoComision(empleado):
	empleado.salario = empleado.salario * 1.03
	return empleado


listaEmpleados2 = map(calculoComision	, listaEmpleados)

for e in listaEmpleados2:
	print(e)
