import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header("Observación e Interpretación de Información de Vehículos")

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # Si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # Generar el histograma usando Plotly Express
    fig = px.histogram(car_data, x='odometer',
                       title="Histograma de Odómetro")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_diagrama = st.checkbox(
    'Construir Diagrama de Dispersión')  # crear una casilla de verificación

if build_diagrama:  # Si la casilla de verificación está seleccionada
    st.write('Creación de un Diagrama de Dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un diagrama de dispersión
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Diagrama de Dispersión de Odómetro vs. Precio")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
