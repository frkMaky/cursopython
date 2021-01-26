from tkinter import *	# Se importa la libreria de interface grafica tkinter (hay otras)

raiz=Tk()				# Se crea la raiz ventana

# Se configura la ventana

raiz.title("Ventana de pruebas")	# Titulo

raiz.resizable(True,True)	# Permitir redimensionar (ancho,alto)

raiz.iconbitmap("hoja.ico")	# Icono de la ventana .iconbitmap(ruta imagen) 

raiz.geometry("650x350")	# Tamaño de la ventana

raiz.config(bg="Blue")		# Color de fondo de la ventana

# Si se cambia la extension del archivo de .py a .pyw (python window) 
# no se habre el terminal al ejecutar el archivo, solo la ventana

raiz.mainloop()			# Se ejecuta la ventana