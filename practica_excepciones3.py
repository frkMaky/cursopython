import math	# Se importa la clase

def calculaRaiz(num1):
	if num1<0:
		raise ValueError("El número no puede ser negativo")
	else:
		return math.sqrt(num1)

# P.Principal -----

op1 = int(input("Introduce un número: "))

try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:	# Se puede especificar un alias del error con la clausula 'as'
	print(ErrorDeNumeroNegativo)

print("Programa terminado.")	# Si salta excepcion no se llega aquí sin controlar las excepciones


#####################################################################################################################
def evaluaEdad(edad):
	# Devuelve un mensaje según la edad pasada por parámetro

	if edad<0:
		raise EdadError("Edad negativa no es posible.")	# raise lanza la excepcion propia EdadError con el mensaje()
	if edad<20:
		return "Eres muy joven."
	elif edad < 40:
		return "Eres joven."
	elif edad < 65:
		return "Eres maduro."
	elif edad < 100:
		return "Cuidate."

# P.Principal -----
while True:	
	edad = int(input("Introduce tu edad:"))
	print(evaluaEdad(edad))
	if edad<0:
		break;