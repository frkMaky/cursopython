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

# Metacaracteres - caracteres comodín

lista_nombres = ["Ana Gómez", "María Martín", "Sandra Lopez" , "Santiago Martín"]

for elemento in lista_nombres:
	# Caracter comodin ^ - que comienze por 
	if (re.findall('^Sandra',elemento)):	
		print(elemento)
	# Caracter comodin $ - que termine por
	if (re.findall('Martín$',elemento)):	
		print(elemento)
	# Caracter comodin [] - que contenga los caracteres en la lista
	if (re.findall('[ñ]',elemento)):	
		print(elemento)

lista_nombres2 = ["Ana",
	"Pedro",
	"María",
	"Rosa",
	"Sandra",
	"Celia"
]
# Rango meta
for elemento in lista_nombres2:
	if re.findall('[^O-T]',elemento):
		print(elemento)

