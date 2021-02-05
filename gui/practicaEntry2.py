from tkinter import *	# Biblioteca de ventanas

raiz = Tk()

miFrame = Frame(raiz,width=650,height=450)				
miFrame.pack()

# Se inicializan variables
minombre=StringVar()	# Cadena de caracteres

cuadroNombre = Entry(miFrame, textvariable=minombre)	    # Cuadros de Texto TEXTBOX
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="?")									# Ocultar contraseña escrita con ?

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

cuadroComentarios = Text(miFrame, width=16, height=5)		# Cuadros de Texto TEXTAREA (width=16, height=5)
cuadroComentarios.grid(row=4, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=cuadroComentarios.yview)	# Configurar scrollbar vertical (yview) para textarea
scrollVert.grid(row=4,column=2, sticky="nsew")	# Se pone scrollbar en el frame / sticky="nsew" para que adaptar tamaño scrollbar al del TEXTAREA
cuadroComentarios.config(yscrollcommand=scrollVert.set)	# Sincronizar textarea y scrollbar

# Etiquetas Cuadros de Texto 

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Contraseña:")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

# Boton
def codigoBoton():	# Rellena el cuadro Nombre con un nombre
	minombre.set("Pablo")

botonEnvio = Button(raiz, text="envíar", command=codigoBoton)	# accion al pulsar el boton command=codigoBoton
botonEnvio.pack()

raiz.mainloop()