import streamlit as st
from utils import load_data

try:
    # Save the dataset in a dataframe
    df = load_data()
    # Streamlit App
    st.set_page_config(page_title="Comparador",
                       page_icon=":crossed_swords:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Title of the home page
    st.title("Comparador",
             text_alignment="center")
    st.divider()
    
except FileNotFoundError:
    print("El archivo o la ruta no existen.")