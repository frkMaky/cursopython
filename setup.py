# Para crear paquetes distribuibles crear archivo setup.py en la raiz
from setuptools import setuptools # Se importa directiva

setup(	# Se define paquete

	name="paquetecalculos",
	version="1.0",
	description="Paquete de ejemplo con calculos basicos",
	author="Pablo",
	author_email="freakghost@gmail.com",
	url="",
	packages=["calculos","calculos.basicos"],
	)


# En la consola de python dirigirse a la capeta de instalación de python
# 
# Ejecutar en dicha carpeta la orden, para este archivo y el paquete/s que 
# contienen convertilos en paquetes distribuibles
#
# python setup.py sdist
#
# Se crean dos carpetas:
# la carpeta dist/ contiene el paquete distribuible 
#
#
# Para intalar el paquete desde el directorio dist/
#
# pip3 install nombre_paquete.tar.gz
#
# Instalado el paquete distribuible, el paquetecalculos se puede importar desde python
#
# para desintarlar el paquete:
#
# pip3 uninstall nombre_paquete.tar.gz