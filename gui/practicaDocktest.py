
def areaTriangulo(base, altura):

	""" 
	Calcula el área de un triángulo dado 

	>>> areaTriangulo(3,6)
	'El área del triángulo es 9.0'

	>>> areaTriangulo(4,5)
	'El área del triángulo es 10.0'

	>>> areaTriangulo(9,3)
	'El área del triángulo es 13.5'

	"""

	return "El área del triángulo es "  + str((base*altura)/2)

def compruebaMail(mailUsuario):

	"""
	Comprueba si un email introducido es válido
	
	>>> compruebaMail('juan@gmail.es')
	True

	>>> compruebaMail('juangmail.es@')
	False

	>>> compruebaMail('juangmail.es')
	False

	>>> compruebaMail('juan@@gmail.es')
	False

	"""
	arroba = mailUsuario.count('@')

	if (arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):

		return False
	else:

		return True


import doctest
doctest.testmod()