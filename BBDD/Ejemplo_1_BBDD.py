import sqlite3 # Libreria BBDD SQLITE

# Abrir o crear conexión

miConexion = sqlite3.connect("PrimeraBase")	# Conectar / crear la BBDD

miCursor = miConexion.cursor()	# Se crea el puntero / cursor

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20) )")	# SQL CREAR TABLA

# miCursor.execute("INSERT INTO PRODUCTOS VALUES ('Balón', 15, 'Deportes')")	# SQL INSERTAR EN TABLA

# Insertar varios
variosProductos = [
	
	("Camiseta", 10, "Deportes"),
	("Jarrón", 90, "Cerámica"),
	("Camión", 20, "Juguetería"),

]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos) 	# Similar a consultas preparadas // Inserción con listas y tuplas

# SQL LEER

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductosLeidos = miCursor.fetchall()

for producto in variosProductosLeidos:
	print(producto)

# Siempre hay que verificar los cambios a realizar en BBDD

miConexion.commit()

miConexion.close()	# Cerrar conexión a BBDD