from tkinter import * # Libreria de ventanas
from tkinter import messagebox	# Ventanas Emergentes

raiz=Tk()	# Se crea ventana

raiz.geometry("1000x600")

def infoAdiciional():
	# Contruye ventana emergente de informacion
	messagebox.showinfo("Titulo", "Mensaje")

def avisoLicencia():
	# Contruye ventana emergente con info licencia
	messagebox.showwarning("Licencia", "Producto bajo licencia libre")

def confirmarSalir():
	# Contruye ventana emergente para confirmar salir

	#valor = messagebox.askquestion("Salir", "¿Desear salir de la aplicacion?")
	valor = messagebox.askokcancel("Salir", "¿Desear salir de la aplicacion?")

	if valor: #Aceptar / OK 
		raiz.destroy()	# Cerrar aplicacion / ventana

def cerrarDocumento():
	# Contruye ventana emergente para cerrar documento

	valor = messagebox.askretrycancel("Cerrar", "No es posible cerrar documento bloqueado")

	if valor: #reintentar
		raiz.destroy()	# Cerrar aplicacion / ventana


barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0) #  tearoff=0 elimina barra separadora por defecto
archivoMenu.add_command(label="Nuevo")	# Submenu
archivoMenu.add_command(label="Guardar")	
archivoMenu.add_command(label="Guardar Como")	
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=confirmarSalir)	
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)	

edicionMenu = Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")

herramientasMenu = Menu(barraMenu, tearoff=0)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de", command=infoAdiciional)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


raiz.mainloop() # Se ejecuta ventana
