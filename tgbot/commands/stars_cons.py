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

def grafico_constelacion(stars, constellations, k):
    """
    Genera un gráfico de constelación.

    Parámetros:
    - stars (pandas.DataFrame): DataFrame que contiene información de las estrellas.
    - constellations (dict): Diccionario que mapea el nombre de la constelación a las estrellas que la conforman.
    - k (int): Índice de la constelación a graficar.

    Retorna:
    - str: Ruta de archivo de la imagen generada.
    """

    # Obtener el nombre de la constelación correspondiente al índice k
    nombre = list(constellations.keys())[k]
    # Obtener las estrellas que conforman la constelación
    estrellas = constellations[nombre]
    # Obtener una lista única de todas las estrellas en la constelación
    estrellas2 = list(set([estrella for tupla in estrellas for estrella in tupla]))

    # Crear una copia del DataFrame de estrellas
    stars2 = stars.copy()
    # Filtrar las estrellas que tienen un nombre no nulo
    stars2 = stars2[stars2['nombre'].notna()]
    # Filtrar las estrellas que se encuentran en la lista estrellas2
    stars2 = [stars2[stars2['nombre'].apply(lambda x: estrella in x)] for estrella in estrellas2]
    # Concatenar los DataFrames resultantes
    stars2 = pd.concat(stars2)

    # Crear un gráfico de dispersión con Plotly
    fig = px.scatter(stars, x='x', y='y', hover_data=[
        'Henry Draper', 'magnitud', 'Harvard Revised', 'nombre'], color_discrete_sequence=['rgba(255, 255, 255, 0.5)'])

    # Agregar líneas que conectan las estrellas de la constelación
    for estrella in estrellas:
        # Obtener las coordenadas de la primera estrella en la tupla
        coordenadas = stars2[stars2['nombre'].apply(lambda x: estrella[0] in x)]
        # Obtener las coordenadas de la segunda estrella en la tupla
        coordenadas2 = stars2[stars2['nombre'].apply(lambda x: estrella[1] in x)]

        # Si se encontraron coordenadas para ambas estrellas, agregar una línea que las conecte
        if len(coordenadas) > 0 and len(coordenadas2) > 0:
            fig.add_trace(go.Scatter(x=[coordenadas['x'].iloc[0], coordenadas2['x'].iloc[0]], y=[coordenadas['y'].iloc[0], coordenadas2['y'].iloc[0]], mode='lines', line=dict(color='red', width=2)))

    # Configurar la posición del texto en los puntos del gráfico
    fig.update_traces(textposition='top center')
    # Configurar el diseño del gráfico
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

    # Guardar el gráfico como una imagen en formato PNG
    output_file = f'tgbot/out/stcons{k}.png'
    fig.write_image(output_file)

    # Retornar la ruta de archivo de la imagen generada
    return output_file
