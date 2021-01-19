
miTupla = ("Juan",13,1,1995) # Las tuplas con () las listas con []

print(miTupla[2]) # Se accede a los elementos de una tupla igual que en una lista

miLista = list(miTupla)     # Convertir una tupla en lista 

miTupla2 = tuple(miLista)   # Convertir una lista en tupla

print(miLista)  # Lista con corchetes  

print(miTupla)  # Tupla con parentesis

print("Juan" in miTupla)    # Comprobar TRUE o FALSE si el elemento esta en la Tupla/Lista

print(miTupla.count(13))  # Contar el nº de elementos indicado (13 en el ejemplo) que están dentro de la tupla (en este caso =1)

tuplaUnitaria = ("Juan",)   # Una Tupla Unitaria con 1 unico elemento se debe declarar con la , final

miTupla3 = "Marisa",14,5,2020   # Una Tupla se puede declarar sin los paréntesis / Empaquetado de Tupla

print(miTupla3)

miTupla4 =("Juan",13,1,1995)

nombre,dia,mes,agno = miTupla4 # declaran varias variables y DESEMPAQUETADO de tupla
print(nombre)
print(dia)
print(mes)
print(agno)

# miTupla4.append("Paco")   # El contenido de las Tuplas no se puede modificar, recortar o ampliar (se puede dividir en otras tuplas)

