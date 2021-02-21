def funcion_decoradora(funcion_parametro):

	def function_interna(*args, **kwargs):
		# Acciones adicionales que decoran
		print("Vamos a realizar un cálculo:")
		funcion_parametro(*args, **kwargs)
		print("Se ha terminado el cáculo")
	return function_interna

@funcion_decoradora
def suma(num1, num2):
	print(num1 + num2)

@funcion_decoradora
def resta(num1, num2):
	print(num1 - num2)

@funcion_decoradora
def potencia(base, exponente):
	print(pow(base,exponente))

suma(7, 5)

resta(12, 10)

potencia(base =5, exponente = 3)