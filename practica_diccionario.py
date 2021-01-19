
# Los diccionarios se declaran entre llaves CLAVE : VALOR 
miDiccionario = {
    "Alemania":"Berlín",
    "Francia":"París",
    "Reino Unido":"Londres",
    "España":"Madrid",
}

print(miDiccionario["España"])  # Se accede por la CLAVE y se obtiene el VALOR

print(miDiccionario)    # Se imprime todo el diccionario

# Agregar un elemento al diccionario

miDiccionario["Italia"] = "Lisboa"    # diccionario[clave] = valor

# Asignar / modificar un valor a una clave concreta se realiza de la misma manera 

miDiccionario["Italia"] = "Roma"    

print(miDiccionario["Italia"])

del miDiccionario["Reino Unido"]    # Se elimina elemento del diccionario > del diccionario[clave]

print (miDiccionario)

# Las claves-valor de un diccionario pueden ser de diferentes tipos de datos
diccionario2 = {
    "Alemania":"Berlin",
    23: "Jordan",
    "Mosqueteros":3,
}

miTupla = ("España","Francia","Reino Unido","Alemania")

miDiccionario3 = {  # Asignar las claves con el contenido de una tupla
    miTupla[0]:"Madrid",
    miTupla[1]:"Paris",
    miTupla[2]:"Londres",
    miTupla[3]:"Berlín",
}

print(miDiccionario3)

miDiccionario4 = {
    23:"Jordan",
    "Nombre":"Michael",
    "Equipo":"Chicago Bulls",
    "Anillos":[1991,1992,1993,1996,1997,1998],  # Se asigna una Tupla como VALOR DE LA CLAVE ANILLOS / tambien se puede asignar otro diccionario como VALOR
}

print (miDiccionario4)

print (miDiccionario4["Equipo"])

print (miDiccionario4["Anillos"])

print(miDiccionario4.keys())    # Devuelve las CLAVES del diccionario

print(miDiccionario4.values())  # Devuelve los VALORES del diccionario

print(len(miDiccionario4))      # Devuelve la longitud del dicionario