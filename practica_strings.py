
nombreUsusario = input("Introduce tu nombre de usuario:\n")

print("El nombre es: ",nombreUsusario)

# Métodos para las cadenas

print("El nombre es: ",nombreUsusario.upper())	# Todo a mayúsculas

print("El nombre es: ",nombreUsusario.lower())	# Todo a minúsculas

print("El nombre es: ",nombreUsusario.capitalize())	# 1ra letra en mayúsculas

edadUsuario = input("Introduce tu edad:\n")

if edadUsuario.isdigit():	# Si lo introducido es un numero
	
	print("Tu edad es ", str(edadUsuario))

else:
	while edadUsuario.isdigit()==False:
		print("¿" + str(edadUsuario) + "?¿tu edad no es un número?")
		print("Vuelve a intentarlo")
		edadUsuario = input("Introduce tu edad:\n")

print("Bienvenido " + nombreUsusario + " y " + edadUsuario + " de edad")

