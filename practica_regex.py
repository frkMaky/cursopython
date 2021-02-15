import re	# Libreria de expresiones regulares

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de síntaxis sencilla."

print (re.search("aprender",cadena))

textoBuscar = "aprender"

if re.search(textoBuscar,cadena) is not None:
	print("He encontrado el texto")
else:
	print("No he encontrado el texto")

textoEncontrado = re.search(textoBuscar,cadena)

print(textoEncontrado.start())

print(textoEncontrado.end())

print(textoEncontrado.span())

textoBuscar2 = "Python"

print(re.findall(textoBuscar2,cadena))

print(len(re.findall(textoBuscar2,cadena)))

