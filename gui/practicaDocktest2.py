import math

def raizCuadrada(listaNumeros):
	""" 
	Devuelve una lista con la raiz cuadrada de los
	elementos pasados por parametros en otra lista 

	>>> lista =[]
	>>> for i in [4,9,16]:
	...	lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]

	>>> lista =[]
	>>> for i in [4,-9,16]:
	...	lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
		...
    ValueError: math domain error

	"""

	return [math.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([9,16,25,36]))

import doctest
doctest.testmod()