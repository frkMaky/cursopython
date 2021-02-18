import re	# Libreria de expresiones regulares

nombre1 = "Sandra Lopez"
nombre2 = "Antonio Lopez"
nombre3 = "María Lopez"
nombre4 = "sandra Lopez"

# Match busca si hay coincidencias al comienzo (siempre al comienzo)
if (re.match("Sandra",nombre1)):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")
#---
if (re.match("Sandra",nombre2)):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")
#---
if (re.match("Sandra",nombre4,re.IGNORECASE)):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")
