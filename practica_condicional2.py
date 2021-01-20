"""
Evalua la concesión de una beca en base a la 3 requisitos:
Distancia > 40 km
Nº Hermanos > 2 (incluyendo al solicitante)
Poder Adquisitivo <= 20000 €/año	!! PESA MAS QUE LAS DEMAS (OR)
"""

print("Programa de becas 2021")
print("----------------------")
print("")
distancia_escuela = int(input("Introduce la distancia a la escuela en km:"))
print("Distancia escuela: " + str(distancia_escuela) + " km")
numero_hermanos = int(input("Introduce el nº de hermanos (incluyendo al solicitante):"))
print("Nº de hermanos: " + str(numero_hermanos))
poder_adquisitivo = int(input("Introduce el poder adquisitivo anual de la unidad familiar en €:"))
print("Poder adquisitivo: " + str(poder_adquisitivo) + " €/año.")
print("----------------------")
if distancia_escuela>40 and numero_hermanos>=2 or poder_adquisitivo<=2000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca, no se cumple alguno de los requisitos")
print("----------------------")