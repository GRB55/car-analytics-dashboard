import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "processed" / "car-dataset-cleaned-2025.csv"

try:
    # Save the dataset in a dataframe
    df = pd.read_csv(DATA_PATH)
    # Streamlit App
    st.set_page_config(page_title="Home",
                       page_icon=":home:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Title of the home page
    st.title("Car Analytics Dashboard",
             text_alignment="center")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(5)
    with tab1:
        st.image(r"Car-analytics-dashboard\images\audi.png", width=300)
    with tab2:
        st.image(r"Car-analytics-dashboard\images\ferrari.png", width=220)
    with tab3:
        st.image(r"Car-analytics-dashboard\images\ford.png", width=300)
    with tab4:
        st.image(r"Car-analytics-dashboard\images\lamborghini.png", width=250)
    with tab5:
        st.image(r"Car-analytics-dashboard\images\mercedes.png", width=300)
    # KPIs
    col6, col7, col8, col9 = st.columns(4)
    with col6:
        st.metric(label="Average Price",
                  value="$" + str(round(df["price"].mean(), 2)),
                  border=True)
    with col7:
        st.metric(label="Average Horse Power",
                  value=round(df["horse_power"].mean(), 2),
                  border=True)
    with col8:
        st.metric(label="Average Top Speed",
                  value=str(round(df["top_speed"].mean(), 2)) + " km/h",
                  border=True)
    with col9:
        st.metric(label="Electric Cars Percentage",
                  value=(len(df[df["engine"] == "electric"]) / len(df)),
                  border=True,
                  format="percent")
    st.title("**Construir una aplicación interactiva en Streamlit que permitía explorar y filtrar los autos de forma dinámica**")
    
except FileNotFoundError:
    print("El archivo o la ruta no existen.")