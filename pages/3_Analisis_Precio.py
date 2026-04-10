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
                           x="brand", y="price", orientation="v", 
                           color_discrete_sequence=['indianred'], 
                           histfunc="avg", category_orders=dict(brand = marcas_ordenadas))
        fig.update_layout(
            xaxis_title_text = "Marca",
            yaxis_title_text = "Precio Promedio"
        )
        st.plotly_chart(fig)
except FileNotFoundError:
    print("El archivo o la ruta no existen.")