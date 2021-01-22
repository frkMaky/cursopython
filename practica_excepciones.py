def suma(num1, num2):
	return num1+num2
def resta(num1, num2):
	return num1-num2
def multiplica(num1, num2):
	return num1*num2
def divide(num1, num2):
	try:								# try .. except para control de excepciones
		return num1/num2
	except ZeroDivisionError:			# except con el tipo de error a controlar
		print("No se puede dividir por 0")
		return "Operación errónea"

while True:	# Se repite la toma de datos hasta que se introduzcan datos numéricos correctamente
	try:
		op1 = int(input("Introduce el primer número:"))
		op2 = int(input("Introduce el segundo número:"))
		break;	# Al introducir datos correctos se sale del bucle infinito
	except ValueError:
		print ("No has introducido datos numéricos. Inténtalo de nuevo.")

operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide):")

if operacion=="suma":
	print(suma(op1,op2))
elif operacion=="resta":
	print(resta(op1,op2))
elif operacion=="multiplica":
	print(multiplica(op1,op2))
elif operacion=="divide":
	print(divide(op1,op2))
else:
	print("Operación no contemplada")

print("Operación ejecutada. Continua la ejecución del programa")	# Esta linea se deberia ejecutar aunque fallen las operaciones (control de excepciones)