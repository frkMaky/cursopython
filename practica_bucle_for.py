# for variable in elemento_a_recorrer:

for i in [1,2,3]:   # For con una lista
    print("Lista: " + str(i) )

for i in ["Primavera","Verano","Otoño","Invierno"]:   # For con una lista
    print("Lista: " + str(i) )

for i in (1,2,3):   # For con una Tupla
    print("Tupla: " + str(i) )

for i in ("Lunes","Martes","Miércoles"):   # For con una Tupla
    print("Tupla: " + str(i) )

for i in ["Pildora","Casa",3]:
	print(str(i) + " - ", end="")	# , end="" como argumento hace que no haya salto de linea en cada vuelta

for i in "Recorriendo_una_cadena":	# Recorrer una cadena con unbucle for
	print(i)

# Comprobar una direccion de email
email = False
punto = 0
direccion = input("Introduce dirección de email:")
for i in direccion:
	if (i=='@'):
		email= True
	if (i=='.'):
		punto +=1
if email and (punto>0):
	print("Email correcto")
else:
	print("Email incorrecto")

# range
for i in range(3):   # For con un rango de 3 elementos: 0 a 2
    print(f"Valor de la variable {i}")	# Notacion print(f"texto {variable} texto")

for i in range(5,10): # Desde 5 hasta 9 
	print (f"Valor: {i}")

for i in range(5,100, 3): # Desde 5 hasta 100 contando de 3 en 3
	print (f"Valor: {i}")

print (len("Longitud de la cadena"))	# Funcion len(str) para devolver la longitud de una cadena

for i in (range(len(direccion))):	# Recorrer un bucle hasta la longitud del email
	print(i)

for letra in "Python":

	if letra=="h":	# Si la letra es h salta a la siguiente vuelta de bucle
		continue	
	print(letra)

for i in direccion:	# For con grupo else
	if i=="@":
		boolArroba = True
		break;	# El break sale del bucle for (incluido el else)
else:	# Se ejecuta cuando terminal el bucle for
	boolArroba = False
print ("La direccion de correo contiene arroba: " +  str(boolArroba))



class miClase:
	pass # Devuelve null - se usa para dejar cosas sin implementar y que el programa no se caiga