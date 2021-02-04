from tkinter import * # Libreria de ventanas

raiz=Tk()	# Se crea ventana

raiz.geometry("1000x600")

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0) #  tearoff=0 elimina barra separadora por defecto
archivoMenu.add_command(label="Nuevo")	# Submenu
archivoMenu.add_command(label="Guardar")	
archivoMenu.add_command(label="Guardar Como")	
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")	
archivoMenu.add_command(label="Cerrar")	

edicionMenu = Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")

herramientasMenu = Menu(barraMenu, tearoff=0)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de")
ayudaMenu.add_command(label="Licencia")


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


raiz.mainloop() # Se ejecuta ventana
