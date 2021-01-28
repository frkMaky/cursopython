from tkinter import *	# Biblioteca de ventanas

root = Tk()	# Se crea ventana raiz

miFrame = Frame(root, width=500, height=400)	# Se cre frame contenedor en la ventana raiz

miFrame.pack()	# Se empaqueta en la ventana raiz el frame


miLabel = Label(miFrame, text="Hola primera label",font=("Comic Sans MS",18),fg="red")	# Se crea un LABEL dentro del contenedor FRAME con las opciones indicadas

#miLabel.pack()	# Limita el tamaño del contenedor al label al hacer pack()

miLabel.place(x=100,y=50)	# Ubica el label en la posicion x,y dentro del contenedor (FRAME)


# Etiqueta con imagen 

miImagen = PhotoImage(file="./pikachu.png")	# Se guarda imagen en una variable

miLabel2 = Label(miFrame, image=miImagen).place(x=100,y=150)	# Se pone imagen en una etiqueta y ubica en el contenedor frame

root.mainloop()	# Se ejecuta la ventana raiz