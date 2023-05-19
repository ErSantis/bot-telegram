import math
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def redondearup(number,n ):
    # redondea hacia abajo con un decimal
    redondeado = math.ceil(number * 10 **n) / 10 **n
    return redondeado


def redondeardown(number, n):
    # redondea hacia abajo con un decimal
    redondeado = math.floor(number * 10 **n) / 10**n
    return redondeado

def grafico_constelacion(stars, constellations,k):
    

    nombre = list(constellations.keys())[k]
    estrellas = constellations[nombre]
    estrellas2 = list(set([estrella for tupla in estrellas for estrella in tupla]))

    stars2 = stars.copy()
    stars2 = stars2[stars2['nombre'].notna()]
    stars2 = [stars2[stars2['nombre'].apply(lambda x: estrella in x)] for estrella in estrellas2]
    stars2 = pd.concat(stars2)

    fig = px.scatter(stars, x='x', y='y', hover_data=[
    'Henry Draper', 'magnitud', 'Harvard Revised', 'nombre'], color_discrete_sequence=['rgba(255, 255, 255, 0.5)'])

    for estrella in estrellas:
        coordenadas = stars2[stars2['nombre'].apply(lambda x: estrella[0] in x)]
        coordenadas2 = stars2[stars2['nombre'].apply(lambda x: estrella[1] in x)]

        if len(coordenadas) > 0 and len(coordenadas2) > 0:
            fig.add_trace(go.Scatter(x=[coordenadas['x'].iloc[0], coordenadas2['x'].iloc[0]], y=[coordenadas['y'].iloc[0], coordenadas2['y'].iloc[0]], mode='lines', line=dict(color='red', width=2)))

    fig.update_traces(textposition='top center')
    fig.update_layout(
        title='Estrellas',
        xaxis_title='Coordenada x',
        yaxis_title='Coordenada y',
        font=dict(family='Arial', size=18, color='white'),
        plot_bgcolor='black',
        paper_bgcolor='black',
        template='plotly_dark',
        width=800,
        height=800
    )
    # Se muestra la figura
    output_file = f'tgbot/out/stcons{k}.png'
    fig.write_image(output_file)
    return output_file