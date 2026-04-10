import streamlit as st
import plotly.express as px
from utils import load_data

try:
    # Save the dataset in a dataframe
    df = load_data()
    # Streamlit page
    st.set_page_config(page_title="Análisis de Precio",
                       page_icon=":bar_chart:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Title of the home page
    st.title("Análisis de Precios",
             text_alignment="center")
    tab1, tab2, tab3 = st.tabs(["Marca", "Combustible", "Correlaciones"])
    with tab1:
        marcas_ordenadas = df.groupby("brand")["price"].mean().sort_values(ascending=False).index
        fig = px.histogram(data_frame=df, 
                           x="brand", y="price",
                           color_discrete_sequence=['indianred'], 
                           histfunc="avg", category_orders=dict(brand = marcas_ordenadas))
        fig.update_layout(
            xaxis_title_text = "Marca",
            yaxis_title_text = "Precio Promedio"
        )
        st.plotly_chart(fig)
        fig1 = px.scatter(data_frame=df,
                          x="horse_power", y="price",
                          color="brand", size="horse_power",
                          color_discrete_sequence=px.colors.sequential.Viridis)
        fig1.update_layout(
            xaxis_title_text = "HP",
            yaxis_title_text = "Precio"
        )
        st.plotly_chart(fig1)
    with tab2:
        combustible_ordenados = df.groupby("fuel_type")["price"].mean().sort_values(ascending=False).index
        fig = px.histogram(data_frame=df, 
                           x="fuel_type", y="price", orientation="v", 
                           color_discrete_sequence=['tomato'], opacity=0.75,
                           histfunc="avg", category_orders=dict(fuel_type = combustible_ordenados))
        fig.update_layout(
            xaxis_title_text = "Combustible",
            yaxis_title_text = "Precio Promedio"
        )
        st.plotly_chart(fig)
        fig1 = px.scatter(data_frame=df,
                          x="horse_power", y="price",
                          color="fuel_type", size="horse_power",
                          color_discrete_sequence=px.colors.sequential.Viridis)
        fig1.update_layout(
            xaxis_title_text = "HP",
            yaxis_title_text = "Precio"
        )
        st.plotly_chart(fig1)
except FileNotFoundError:
    print("El archivo o la ruta no existen.")