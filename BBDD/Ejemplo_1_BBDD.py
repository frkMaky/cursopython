import sqlite3 # Libreria BBDD SQLITE

# Abrir o crear conexión

miConexion = sqlite3.connect("PrimeraBase")	# Conectar / crear la BBDD

miCursor = miConexion.cursor()	# Se crea el puntero / cursor

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20) )")	# SQL

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('Balón', 15, 'Deportes')")	# SQL

# Siempre hay que verificar los cambios a realizar en BBDD

miConexion.commit()

miConexion.close()	# Cerrar conexión a BBDD