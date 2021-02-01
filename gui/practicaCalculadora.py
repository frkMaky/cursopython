from tkinter import * # Libreria de ventanas

raiz=Tk()	# Se crea ventana

miFrame = Frame(raiz)	# Se pone frame en la ventana
miFrame.pack()			# Se empaqueta todo en la ventana

operacion=""	# Operacion a realizar variable GLOBAL

resultado = 0	# Resultado de la operacion

# Pantalla --------------------------------------------------

numeroPantalla=StringVar()	# Nª a mostrar en la pantalla

pantalla = Entry(miFrame, textvariable=numeroPantalla)		# Se asocia la variable a la pantalla
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)	# columnspan=4 para ocupar 4 columnas de ancho
pantalla.config(bg="black", fg="green", justify="right")

# Pulsaciones teclado ----------------------------------------

def numeroPulsado(num):
	global operacion # Se utiliza variable GLOBAL

	if operacion != "":	# Si se ha pulsado operacion no se sigue concatenando numero
		numeroPantalla.set(num)
		operacion=""
	else:
		numeroPantalla.set(numeroPantalla.get() + str(num))

# El Resultado ----------------------------------------

def el_resultado():
	global resultado

	numeroPantalla.set(resultado + int(numeroPantalla.get()))	# Se pone el resultado en pantalla

# Suma ----------------------------------------
def suma(num):
	global operacion # Se utiliza variable GLOBAL
	global resultado

	resultado += int(num)	# Se suma al resultado el valor del nº en pantalla
	operacion="suma"
	numeroPantalla.set(resultado)	# Se pone el resultado en pantalla

# BOTONES POR FILA-------------------------------------------------
# 789% ------------------------------------------------------------
boton7 = Button(miFrame,text="7",width=3, command=lambda:numeroPulsado("7")).grid(row=2,column=1)
boton8 = Button(miFrame,text="8",width=3, command=lambda:numeroPulsado("8")).grid(row=2,column=2)
boton9 = Button(miFrame,text="9",width=3, command=lambda:numeroPulsado("9")).grid(row=2,column=3)
botonDiv = Button(miFrame,text="%",width=3).grid(row=2,column=4)
# 456X --------------------------------------------------
boton4 = Button(miFrame,text="4",width=3, command=lambda:numeroPulsado("4")).grid(row=3,column=1)
boton5 = Button(miFrame,text="5",width=3, command=lambda:numeroPulsado("5")).grid(row=3,column=2)
boton6 = Button(miFrame,text="6",width=3, command=lambda:numeroPulsado("6")).grid(row=3,column=3)
botonMult = Button(miFrame,text="X",width=3).grid(row=3,column=4)
# 123-  --------------------------------------------------
boton1 = Button(miFrame,text="1",width=3, command=lambda:numeroPulsado("1")).grid(row=4,column=1)
boton2 = Button(miFrame,text="2",width=3, command=lambda:numeroPulsado("2")).grid(row=4,column=2)
boton3 = Button(miFrame,text="3",width=3, command=lambda:numeroPulsado("3")).grid(row=4,column=3)
botonRest = Button(miFrame,text="-",width=3).grid(row=4,column=4)
# 0.=+  --------------------------------------------------
boton0 = Button(miFrame,text="0",width=3, command=lambda:numeroPulsado("0")).grid(row=5,column=1)
botonComa = Button(miFrame,text=".",width=3).grid(row=5,column=2)
botonIgual = Button(miFrame,text="=",width=3, command=lambda:el_resultado()).grid(row=5,column=3)
botonSuma = Button(miFrame,text="+",width=3, command=lambda:suma(numeroPantalla.get())).grid(row=5	,column=4)
#------------------------------------------------------------------

raiz.mainloop()	# Se ejecuta ventana
