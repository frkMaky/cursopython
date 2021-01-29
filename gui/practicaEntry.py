from tkinter import *	# Biblioteca de ventanas

root = Tk()	# Se crea ventana raiz

miFrame = Frame(root,width=600,height=400)
miFrame.pack()

"""
miLabel = Label(miFrame,text="Nombre:")
#miLabel.place(x=50,y=50)
miLabel.grid(row=0,column=0)		# Colocacion en el contenedor GRID (row, column)
# Cuadro de Texto -----------------------------------
cuadroTexto = Entry(miFrame)
#cuadroTexto.place(x=100,y=50)
cuadroTexto.grid(row=0,column=1)
# ---------------------------------------------------
"""

# con .grid(row=0,column=0) se colocan los widgets/elementos de formulacio en la posición en la tabla
# sticky para ubicarlos por coordenadas geográficas
# padx y pady para separacion con los bordes


cuadroNombre = Entry(miFrame).grid(row=0,column=1, pady=4, padx=5)
cuadroApellido = Entry(miFrame).grid(row=1,column=1, pady=4, padx=5)
cuadroDireccion = Entry(miFrame).grid(row=2,column=1, pady=4, padx=5)
labelNombre = Label(miFrame,text="Nombre:").grid(row=0,column=0, sticky="e", pady=4, padx=5)
labelApellido = Label(miFrame,text="Apellido:").grid(row=1,column=0, sticky="e", pady=4, padx=5)
labelDireccion = Label(miFrame,text="Direccion:").grid(row=2,column=0, sticky="e", pady=4, padx=5)


root.mainloop()	# Se ejecuta la ventana raiz
