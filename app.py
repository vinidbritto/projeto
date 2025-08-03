import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header("Análise Exploratória de Dados")

if st.checkbox("Mostrar Dados de Quilometragem"):
    st.write('Criando histograma para o conjunto de dados de vendas de veículos')
    fig = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True, key='histogram_plot')


if st.checkbox("Mostrar Dados de Preço"):
    st.write('Criando gráfico de dispersão enrte preço e quilometragem')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True, key='scatter_plot')
    
    