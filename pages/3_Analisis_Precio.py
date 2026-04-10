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
except FileNotFoundError:
    print("El archivo o la ruta no existen.")