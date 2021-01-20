print("Valoración de notas")

def evaluacion(nota):
	# Comprueba si con la nota esta aprobado o suspenso
	valoracion = "aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

nota_alumno = int(input("Introduce la nota:"))	# Se introduce la nota del alumno por teclado y se cambia de str a int

print(evaluacion(nota_alumno))