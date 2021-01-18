
miLista = ["María","Pepe","Marta","Antonio"]

print(miLista[:])   #Imprime toda la lista

print(miLista[-2])   #Imprime el elemento menos -2 de la lista (hacia atrás)

print(miLista[2:])   #Imprime desde indice 2 (incluido) hasta el final 

print(miLista[:2])   #Imprime desde el principio hasta el indice 2 (no incluido)

miLista.append("Sandra") #Agregar elemento al final de la lista

miLista.insert(4,"Manuel") #Agrega el elemento en el indice indicado

miLista.extend(["Sara","Merchi","Lucia"]) #Agregar varios elementos (otra lista concatenada)

print(miLista[:])

print(miLista.index("Marta")) #Devuelve el indice de la lista

print("Pepe" in miLista) #True o False si el elemento esta en la lista

miLista.remove("Marta") # Elimina un elemento

miLista.pop() # Elimina el ULTIMO elemento de la lista

miLista = ["María",5, True, 78.95] # Una lista puede contener diferentes tipos de elementos

miLista2 = ["Sandra","Lucía"]

miLista3 = miLista + miLista2 # concatenar listas (operador +)

print(miLista3[:])

print (miLista[:] *  3) # Repetir una lista