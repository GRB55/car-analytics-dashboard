import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed"

try:
    file = DATA_PATH / "car-dataset-cleaned-2025.csv"
    df = pd.read_csv(file)
    # Streamlit App
    st.set_page_config(page_title="EDA",
                       page_icon=":graph:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Title of the home page
    st.title("Exploratory Data Analysis",
             text_alignment="center")
    
    container = st.container()
    with container:
        st.bar_chart(data=df, y="brand")
    
except FileNotFoundError:
    print("El archivo o la ruta no existen.")