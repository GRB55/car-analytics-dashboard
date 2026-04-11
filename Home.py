import streamlit as st
import pandas as pd
from utils import load_data

try:
    # Guardar el dataset en un marco de datos
    df = load_data()
    # Streamlit App
    st.set_page_config(page_title="Home",
                       page_icon=":house:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Titulo de la home page
    st.title("CarInsight 2025",
             text_alignment="center")
    # Objetivo de la app
    st.markdown("""
                **CarInsight** es una aplicación interactiva de análisis del mercado automotor global 2025. A partir de un dataset de autos de distintas marcas y características técnicas, permite explorar, comparar y entender qué hay detrás del precio de un auto, e incluso predecirlo.
                """,
                text_alignment="left")
    st.divider()
    st.markdown("""
                La app está dividida en cuatro secciones:\n
                - `Explorador` — navegá el dataset completo con filtros por marca, combustible, precio y potencia. Exportá los resultados que te interesen.
                - `Comparador` — elegí dos autos y enfrentalos cara a cara: specs técnicos, precio y rendimiento en un gráfico de radar.
                - `Análisis de Precio` — descubrí qué variables impactan más en el precio a través de gráficos de distribución, dispersión y correlaciones.
                - `Predictor` — ingresá las características de un auto y obtené una estimación de precio basada en un modelo de Machine Learning entrenado con los datos del dataset.
                """)
    # KPIs
    st.header("**Métricas generales**")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric(label="Precio Promedio",
                  value="$" + str(round(df["price"].mean(), 2)),
                  border=True)
    with col2:
        st.metric(label="Promedio de Caballos de Fuerza",
                  value=str(round(df["horse_power"].mean(), 2)) + " hp",
                  border=True)
    with col3:
        st.metric(label="Velocidad Máxima Promedio",
                  value=str(round(df["top_speed"].mean(), 2)) + " km/h",
                  border=True)
    with col4:
        st.metric(label="Porcentaje de Autos Eléctricos",
                  value=(len(df[df["engine"] == "electric"]) / len(df)),
                  border=True,
                  format="percent")
    with col5:
        st.metric(label="Cantidad de Marcas",
                  value=len(df["brand"].unique()),
                  border=True)
    with col6:
        st.metric(label="Cantidad de Modelos",
                  value=len(df["model"].unique()),
                  border=True,
                  format="compact")
    marcas = df["brand"].str.title().sort_values().unique()
    st.dataframe(pd.DataFrame(marcas, columns=["Marca"]))
except FileNotFoundError:
    print("El archivo o la ruta no existen.")