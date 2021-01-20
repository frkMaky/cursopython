"""
Programa para escoger asignatura optativa de un listado dado

El programa verifica si la asignatura escogida es correcta
"""
print("Asignaturas optativas")
print("---------------------")
print("")
print("Informática gráfica")
print("Pruebas de software")
print("Usabilidad y Accesibilidad")
print("")
print("")
opcion = input("Introduce la asignatura escogida:")

asignatura = opcion.lower()	# Se formatea lo introducido todo a minusculas

# Operado in 
if asignatura in ("informática gráfica","pruebas de software","usabilidad y accesibilidad"):
	print("Asignatura optativa: " +  asignatura)
else:
	print("La asinatura " + asignatura + " no se encuentra en las disponibles")
