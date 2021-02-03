from tkinter import * # Libreria de ventanas

raiz=Tk()	# Se crea ventana

raiz.title("Checkbutton")

playa = IntVar()
montagna = IntVar()
turismoRural = IntVar()

def opcionViaje():
	opcionEscogida = ""
	if(playa.get()==1):
		opcionEscogida += " playa"
	if(montagna.get()==1):
		opcionEscogida += " montaña"
	if(turismoRural.get()==1):
		opcionEscogida += " turismo rural"

	textoFinal.config(text=opcionEscogida)

foto = PhotoImage(file="./pikachu.png")
Label(raiz,image=foto).pack()

frame = Frame(raiz).pack()
Label (frame, text="Elige destino:", width=50).pack()
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionViaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna , onvalue=1, offvalue=0, command=opcionViaje).pack()
Checkbutton(frame, text="Turismo Rural", variable=turismoRural , onvalue=1, offvalue=0, command=opcionViaje).pack()

textoFinal = Label(frame).pack()

raiz.mainloop()	# Se ejecuta ventana