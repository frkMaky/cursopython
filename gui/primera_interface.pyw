from tkinter import *	# Se importa la libreria de interface grafica tkinter (hay otras)

raiz=Tk()				# Se crea la raiz ventana

# Se configura la ventana

raiz.title("Ventana de pruebas")	# Titulo

raiz.resizable(True,True)	# Permitir redimensionar (ancho,alto)

raiz.iconbitmap("hoja.ico")	# Icono de la ventana .iconbitmap(ruta imagen) 

# raiz.geometry("650x350")	# Tamaño de la ventana (la raiz se adapta al tamaño del Frame)

raiz.config(bg="Blue")		# Color de fondo de la ventana

# Si se cambia la extension del archivo de .py a .pyw (python window) 
# no se habre el terminal al ejecutar el archivo, solo la ventana

miFrame = Frame()		# Se crea una lámina (donde iran los widgets)

miFrame.config(bg="Red")	# Color de fondo de la lámina

miFrame.config(width="650", height="350")	# Tamaño de la lámina (al redimensionar la ventana se distingue entre raiz/frame)

miFrame.config(bd=35) # Ancho del borde del frame
 	
miFrame.config(cursor="hand2")	# Cursor sobre el frame

miFrame.config(relief="groove")	# Borde del frame

miFrame.pack(fill="y", expand=True)	# Rellenado y permitir expandir frame al redimensionar

miFrame.pack(side="left",anchor="n") # Se empaqueta la lamina (admite opciones)

raiz.mainloop()			# Se ejecuta la ventana


