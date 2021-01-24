def divide():
	# Realiza la división de los nº que solicita
	try:
		op1 = float(input("Introduce el dividendo:"))
		op2 = float(input("Introduce el divisor:"))
		print("La división de " +  str(op1) + " con " + str(op2) +  " es " + str(op1/op2))
	except ValueError:								# Excepciones en cadena para controlar 
		print("El valor introducido es erróneo")
	except ZeroDivisionError:						# distintos tipos de error individualmente
		print("No se puede dividir por 0.")
	except:											# Para error genérico no se especifica 
		print("Ha ocurrido un error")
	finally:										# clausula finally para código que debe ejecutarse siempre (con o sin errores)
		print("Cálculo finalizado")	


divide()