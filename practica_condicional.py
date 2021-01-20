# Evalúa los salarios de unos empleados

salario_presidente = int(input("Salario presidente:"))
print ("El salario del presidente: " +  str(salario_presidente)  +" €")

salario_director = int(input("Salario director:"))
print ("El salario del director: " +  str(salario_director)  +" €")

salario_jefe_area = int(input("Salario jefe área:"))
print ("El salario del jefe área: " +  str(salario_jefe_area)  +" €")

salario_administrativo = int(input("Salario administrativo:"))
print ("El salario del administrativo: " +  str(salario_administrativo)  +" €")

# Comprueba el orden jerarquíco de los empleados por salario
if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")

