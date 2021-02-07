import sqlite3 # Libreria BBDD SQLITE

miConexion = sqlite3.connect("GestionProductos")	# Conectar / crear la BBDD

miCursor = miConexion.cursor()	# Se crea el puntero / cursor

# Creación de TABLA con clave primaria 

miCursor.execute('''
	CREATE TABLE PRODUCTOS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

# Se insertan varios productos en la tabla creada
productos = [
	("pelota", 20, "juguetería"),
	("pantalón", 15, "confección"),
	("destornillador", 25, "ferretería"),
	("jarrón", 45, "cerámica"),
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos) 

miConexion.commit()

# Se recuperan los registros de la tabla y se muestran por pantalla 

miCursor.execute("SELECT * FROM PRODUCTOS")	

listado = miCursor.fetchall()

for producto in listado:

	print("Código:", producto[0]," Producto: ", producto[1], " Precio: ", producto[2], " Sección: ", producto[3])

miConexion.commit()

miConexion.close()	# Cerrar conexión a BBDD