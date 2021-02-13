"""
def numeropar(num):
	if num%2==0:
		return True
"""

numeros = [17,24,28,7,39,25,36,15]

print(list(filter(lambda numeropar: numeropar%2==0,numeros)))


class Empleado:

	def __init__(self,nombre,cargo,salario):
		self.nombre =nombre 
		self.cargo =cargo 
		self.salario =salario

	def __str__(self):
		return "{} que trabaja como {} y tiene un salario de {}".format(self.nombre,self.cargo,self.salario)

listaEmpleados =[
Empleado("Juan","Director",75000),
Empleado("Ana","Presidenta",85000),
Empleado("Antonio","Administrativo",25000),
Empleado("Sara","Secretaria",27000),
Empleado("Mario","Botones",21000),
]

salariosAltos = filter(lambda empleado: empleado.salario>50000, listaEmpleados)

for salario in salariosAltos:
	print(salario)
