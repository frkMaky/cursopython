def funcion_decoradora(funcion_parametro):
	def function_interna():
		# Acciones adicionales que decoran
		print("Vamos a realizar un cálculo:")
		funcion_parametro()
		print("Se ha terminado el cáculo")
	return function_interna

@funcion_decoradora
def suma():
	print(15+20)

@funcion_decoradora
def resta():
	print(30-10)

suma ()
resta ()