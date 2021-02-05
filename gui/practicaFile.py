from tkinter import * # Libreria de ventanas
from tkinter import filedialog	# Ventanas de archivos

raiz=Tk()	# Se crea ventana

def abreFichero():

	fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetype=(("Ficheros de excel","*.xlsx"),("Ficheros de Texto","*.txt"),("Todos los ficheros","*.*")))

	print(fichero)


boton = Button(text="Abrir Fichero", command=abreFichero)
boton.pack()


raiz.mainloop()