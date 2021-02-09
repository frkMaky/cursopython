from tkinter import *			# Libreria de ventanas
from tkinter import messagebox	# Ventanas emergentes
import sqlite3					# BBDD sqlite

# ---------------------------------------------------------------------------

def conexionBBDD():	# Crea la BBDD de usuarios
	
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE DATOSUSUARIO (
			ID INTEGER PRIMARY KEY AUTOINCREMENT, 
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(100),
			COMENTARIOS VARCHAR(250))
			''')
		messagebox.showinfo("BBDD","BBDD creada con éxito")
	except:
		messagebox.showwarning("¡Atención!","La BBDD ya existe")

def salirAplicacion(): # Sale de la aplicación al confirmar
	
	valor = messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")

	if valor=="yes":
		root.destroy()

def limpiarCampos(): # Borra los campos del formulario
	varID.set("")
	varNombre.set("")
	varApellido.set("")
	varDireccion.set("")
	varPassword.set("")
	cuadroComentarios.delete(1.0,END)

def crear():	# CRUD - Inserta nuevo registro
	
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	miCursor.execute("INSERT INTO DATOSUSUARIO VALUES(NULL,'" +  varNombre.get() + "','" + varPassword.get() + "','" + varApellido.get() + "','" + varDireccion.get() + "','" + cuadroComentarios.get("1.0",END) + "')") 
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro insertado con éxito")


# ---------------------------------------------------------------------------
root = Tk()	# Ventana principal 

# Aspecto ventana principal -----
root.title("CRUD Usuarios")	# Titulo
root.resizable(True,True)			# Permitir redimensionar (ancho,alto)
root.iconbitmap("hoja.gif")			# Icono de la ventana .iconbitmap(ruta imagen) 
root.geometry("650x450")			# Tamaño de la ventana
root.config(bg="gray")				# Color de fondo de la ventana
# ------------------------------

# Barra de Menus --------------
barraMenu = Menu(root)								# Se crea menu en la ventana principal
root.config(menu=barraMenu, width=300, height=300)	# y se vincula

# Opciones del Menu - BBDD
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Cerrar", command=salirAplicacion)
# Opciones del Menu - Borrar
borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)
# Opciones del Menu - CRUD
crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")
# Opciones del Menu - Ayuda
ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

# Se añaden opciones a la barra de menus
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
#------------------------------

# FRAME FORMULARIO ----------------------

formularioFrame = Frame(root)
formularioFrame.pack()

# Variables para los campos de texto
varID = StringVar()
varNombre = StringVar()
varApellido = StringVar()
varDireccion = StringVar()
varPassword = StringVar()

cuadroId = Entry(formularioFrame, textvariable=varID).grid(row=0,column=1, padx=10, pady=10)

cuadroNombre = Entry(formularioFrame, textvariable=varNombre)
cuadroNombre.config(justify="right",fg="red")
cuadroNombre.grid(row=1,column=1, padx=10, pady=10)

cuadroPassword = Entry(formularioFrame,textvariable=varPassword)
cuadroPassword.config(show="?")
cuadroPassword.grid(row=2,column=1, padx=10, pady=10)

cuadroApellido = Entry(formularioFrame, textvariable=varApellido)
cuadroApellido.grid(row=3,column=1, padx=10, pady=10)

cuadroDireccion = Entry(formularioFrame, textvariable=varDireccion)
cuadroDireccion.grid(row=4,column=1, padx=10, pady=10)

cuadroComentarios = Text(formularioFrame,width=20,height=5)	#Area de comentarios
cuadroComentarios.grid(row=5,column=1, padx=10, pady=10)				

scrollComentarios = Scrollbar(formularioFrame,command=cuadroComentarios.yview)	#Barra de scroll a la derecha
scrollComentarios.grid(row=5,column=2, sticky="nsew")	

cuadroComentarios.config(yscrollcommand=scrollComentarios.set)	#Se sincroniza con la barra

# Etiquetas
idLabel = Label(formularioFrame,text="ID: ")
idLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(formularioFrame,text="Nombre: ")
nombreLabel.grid(row=1,column=0, padx=10, pady=10)

passwordLabel = Label(formularioFrame,text="Password: ")
passwordLabel.grid(row=2,column=0, padx=10, pady=10)

apellidoLabel = Label(formularioFrame,text="Apellido/s: ")
apellidoLabel.grid(row=3,column=0, padx=10, pady=10)

direccionLabel = Label(formularioFrame,text="Dirección: ")
direccionLabel.grid(row=4,column=0, padx=10, pady=10)

comentariosLabel = Label(formularioFrame,text="Comentarios: ")
comentariosLabel.grid(row=5,column=0, padx=10, pady=10)

# ----------------------------------------
# FRAME BOTONES ----------------------
botonesFrame = Frame(root)

botonCrear = Button(botonesFrame,text="Create", command=crear)
botonCrear.grid(row=1,column=0, sticky="e",padx=10, pady=10)

botonLeer = Button(botonesFrame,text="Read")
botonLeer.grid(row=1,column=1, sticky="e",padx=10, pady=10)

botonActualizar = Button(botonesFrame,text="Update")
botonActualizar.grid(row=1,column=2, sticky="e",padx=10, pady=10)

botonBorrar = Button(botonesFrame,text="Delete")
botonBorrar.grid(row=1,column=3, sticky="e",padx=10, pady=10)

botonesFrame.pack()
# ------------------------------------



root.mainloop()	# Ventana principal - ejecutar
