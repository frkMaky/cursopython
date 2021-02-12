"""
def area_triangulo(base,altura):

	return (base*altura)/2

"""

# lambda - funciones anónimas - simplificacion de código 

area_triangulo = lambda base,altura:(base*altura)/2	# lambda 

print(area_triangulo(5,7))

print(area_triangulo(9,6))

triangulo1 = area_triangulo(5,7)

triangulo2 = area_triangulo(9,6)

print(triangulo1)

print(triangulo2)

eleva_al_cubo = lambda base: base**3	# lambda 
	
print(eleva_al_cubo(2))

al_cubo = lambda base:pow(base,3)	# lambda 

print(al_cubo(4))

destacar_valor = lambda comision:"¡{}! €".format(comision) # lambda - dar formato

comision_Ana = 15585 

print(destacar_valor(comision_Ana))