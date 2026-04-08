import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed"

try:
    file = DATA_PATH / "car-dataset-cleaned-2025.csv"
    df = pd.read_csv(file)
    # Streamlit App
    st.set_page_config(page_title="Home",
                       page_icon=":home:",
                       layout="wide",
                       initial_sidebar_state="auto")
    # Title of the home page
    st.title("Car Analytics Dashboard",
             text_alignment="center")
    container = st.container()
    with container:
        st.image(r"Car-analytics-dashboard\images\png-transparent-laferrari-car-logo-scuderia-ferrari-ferrari-horse-emblem-logo-thumbnail.png")
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Average Price",
                  value="$" + str(round(df["price"].mean(), 2)),
                  border=True)
    with col2:
        st.metric(label="Average Horse Power",
                  value=round(df["horse_power"].mean(), 2),
                  border=True)
    with col3:
        st.metric(label="Average Top Speed",
                  value=str(round(df["top_speed"].mean(), 2)) + " km/h",
                  border=True)
    with col4:
        st.metric(label="Electric Cars Percentage",
                  value=(len(df[df["engine"] == "electric"]) / len(df)),
                  border=True,
                  format="percent")
    st.title("**Construir una aplicación interactiva en Streamlit que permitía explorar y filtrar los autos de forma dinámica**")
except FileNotFoundError:
    print("El archivo o la ruta no existen.")