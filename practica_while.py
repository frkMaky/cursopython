import math

i = 1

while i<=10: # Imprime mientras sea menor o igual a 10
    print("Vuelta " + str(i))
    i +=1

print("Terminó la ejecución")

""" Programa que pregunta la edad """

edad = int(input("Introduce tu edad:"))

while edad<0 or edad>100:   # Edad de 0 a 100 años
    print("Has introducido una edad errónea. Vuelve a intentarlo:")
    edad = int(input("Introduce tu edad:"))
print("Tu edad es: "  + str(edad) + " años")

""" Programa que averigua la raíz cuadrada de un número """

print("Programa de cálculo de raíz cuadrada")

numero = int(input("Introduce un número:"))
intentos = 0

while numero<0:
    print("No se puede hallar la raíz cuadrada de un número negativo")

    if intentos==2:
        print("Has utilizado demasiados intentos. El programa finalizará")
        break;  # Termina el bucle
    numero = int(input("Introduce un número:")) 
    if numero<0:
        intentos +=1

if intentos<2:
    solucion= math.sqrt(numero)
    print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))