
# Funcion para leer el archivo stars.txt
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def read_stars():
	data = []
	with open('tgbot/constellations/stars.txt', 'r') as file:
		for line in file:
			# Separar los valores en 7 columnas
			columns = line.split()
			# Verificar si la columna 7 tiene más de un nombre
			if len(columns) > 6:
				# Crear una lista de nombres separados por ";"
				# seleccionar de la columna 7 en adelante
				name = ' '.join(columns[6:])
				# quitar los saltos de linea
				name = name.replace('\n', '')
				# separar los nombres por ";"
				name = name.split(';')
 				# eliminar los espacios vacios al inicio y al final
				name = [n.strip() for n in name]
				columns = columns[:6] + [name]
			data.append(columns)
	# Crear un dataframe con los datos
	stars = pd.DataFrame(data, columns=[
            'x', 'y', 'z', 'Henry Draper', 'magnitud', 'Harvard Revised', 'nombre'])
	# Convertir las columnas x, y y z a float
	stars['x'] = stars['x'].astype(float)
	stars['y'] = stars['y'].astype(float)
	stars['z'] = stars['z'].astype(float)
	# eliminar la columna z
	stars = stars.drop(columns=['z'])

	# print('Se ha leido el archivo stars.txt')
	# print('El dataframe tiene', len(stars),
	#       'filas y', len(stars.columns), 'columnas')
	# print('Las columnas son:', stars.columns)
	# print('Los primeros 5 registros son:')
	# print(stars.head())

	# Se retorna el dataframe
	return stars

# print(read_stars())

# Funcion para leer los archivos de las constelaciones


def read_constellations():
	# Se crea un diccionario vacio para guardar las constelaciones
	constellations = {}
	# Se recorren los archivos de la carpeta constellations
	for file in os.listdir('tgbot/constellations'):
		# excluye el archivo stars.txt
		if file == 'stars.txt':
			continue
		# Se lee el archivo
		archivo = open('tgbot/constellations/' + file, 'r')
		# Se crea una lista vacia para guardar las estrellas de la constelacion
		estrellas = []
		# Se recorren las lineas del archivo
		for linea in archivo:
			# Se separa la linea por espacios
			linea = linea.split(',')
			# quitar los saltos de linea
			linea[1] = linea[1].replace('\n', '')
			# se guardar la tupla con las estrellas
			estrellas.append((linea[0], linea[1]))
		# quita la extension del archivo
		file = file.split('.')[0]
		# Se guarda la lista de estrellas en el diccionario
		constellations[file] = estrellas

	# print('Se han leido los archivos de las constelaciones')
	# print('El diccionario tiene', len(constellations), 'constelaciones')
	# print('Las constelaciones son:', constellations.keys())
	# print(constellations)

	# Se retorna el diccionario
	return constellations

# print(read_constellations())

# Funcion para mostrar un grafico con todas las estrellas


def grafico_estrellas(stars):

	# Se crea una figura
	# fig = px.scatter(stars, x='x', y='y', hover_data=[
	#  'Henry Draper', 'magnitud', 'Harvard Revised', 'nombre'])
	# Asignar colores por magnitud
	fig = px.scatter(stars, x='x', y='y', hover_data=[
            'Henry Draper', 'magnitud', 'Harvard Revised', 'nombre'], color='magnitud', color_continuous_scale='viridis')

	# Personalizar el gráfico
	fig.update_traces(textposition='top center')
	fig.update_layout(
		title='Estrellas',
		xaxis_title='Coordenada x',
		yaxis_title='Coordenada y',
		font=dict(
			family='Arial',
			size=18,
			color='white'
		),
            xaxis=dict(
                    tickmode='linear',
                    tick0=0,
                    dtick=0.1,
                    range=[-1, 1.1]
            ),
            yaxis=dict(
                    tickmode='linear',
                    tick0=0,
                    dtick=0.1,
                    range=[-1, 1.1]
            ),
            plot_bgcolor='black',
            paper_bgcolor='black',
            template='plotly_dark'

	)
	# Se muestra la figura
	# fig.show()
	# Se guarda la figura
	output_file = 'tgbot/out/estrellas.png'
	fig.write_image(output_file, width=1000, height=1000)
	return output_file
	
