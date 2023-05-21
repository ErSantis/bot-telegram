

import math
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def dibujar_constelacion(fig, stars, estrellas, nombre, color):
    # separar las tuplas
    estrellas2 = [estrella for tupla in estrellas for estrella in tupla]
    estrellas2 = list(set(estrellas2))
    # print(estrellas2)
    # crear una copia de stars
    stars2 = stars.copy()
    # eliminar las filas donde el nombre sea None
    stars2 = stars2[stars2['nombre'].notna()]
    stars2 = [stars2[stars2['nombre'].apply(
        lambda x: estrella in x)] for estrella in estrellas2]
    # convertirlo a dataframe
    stars2 = pd.concat(stars2)
	# Se agregan las lineas de la constelacion
    for estrella in estrellas:
        # Se obtienen las coordenadas de las estrellas, buscando por el nombre
        coordenadas = stars2[stars2['nombre'].apply(
            lambda x: estrella[0] in x)]
        coordenadas2 = stars2[stars2['nombre'].apply(
            lambda x: estrella[1] in x)]

        # Se agregan las lineas de color rojo y gruesas
        if(len(coordenadas) > 0 and len(coordenadas2) > 0):
            fig.add_trace(go.Scatter(x=[coordenadas['x'].iloc[0], coordenadas2['x'].iloc[0]], y=[coordenadas['y'].iloc[0], coordenadas2['y'].iloc[0]], mode='lines',name=nombre, line=dict(
                color=color, width=2)))


def get_constellation_df(stars, estrellas):
	# separar las tuplas
	estrellas2 = [estrella for tupla in estrellas for estrella in tupla]
	estrellas2 = list(set(estrellas2))
	# print(estrellas2)
	# crear una copia de stars
	stars2 = stars.copy()
	# eliminar las filas donde el nombre sea None
	stars2 = stars2[stars2['nombre'].notna()]
	stars2 = [stars2[stars2['nombre'].apply(
		lambda x: estrella in x)] for estrella in estrellas2]
	# convertirlo a dataframe
	stars2 = pd.concat(stars2)
	return stars2

def grafico_constelaciones(stars, constellations):
    # se obtienen solo las estrellas que estan en las constelaciones
    # crear un df vacio
    df = pd.DataFrame(
        columns=['x', 'y', 'Henry Draper', 'magnitud', 'Harvard Revised', 'nombre'])

    for constellation in constellations.values():
        df = pd.concat([df, get_constellation_df(stars, constellation)])


	# Make the dots white
    fig = px.scatter(stars, x='x', y='y', hover_data=[
    'Henry Draper', 'magnitud', 'Harvard Revised', 'nombre'], color_discrete_sequence=['rgba(255, 255, 255, 0.5)'])
    
    # Personalizar el gráfico
    offset = 2
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
            range=[-1, 1]
        ),
        yaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=0.1,
            range=[
                -1, 1
            ]
        ),
        plot_bgcolor='black',
        paper_bgcolor='black',
        template='plotly_dark',
        width=800,
        height=800

    )

    # asigna un color a cada constelacion
    colors = px.colors.qualitative.Plotly
    for i, (nombre, constellation) in enumerate(constellations.items()):
        dibujar_constelacion(fig, stars, constellation, nombre, colors[i])
        x=1.1,
        y=0.9 - i * 0.05,
        xref="paper",
        yref="paper",
        text=nombre,
        showarrow=False,
        font=dict(color=colors[i])
    
    output_file = f'tgbot/out/stcons.png'
    fig.write_image(output_file)
    return output_file