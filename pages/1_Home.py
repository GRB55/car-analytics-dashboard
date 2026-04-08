import streamlit as st
import pandas as pd
from load_data import load_data

try:
    df = load_data()
    # Streamlit App
    st.set_page_config(page_title="Home",
                       page_icon=":home:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Title of the home page
    st.title("Car Analytics Dashboard",
             text_alignment="center")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(r"Car-analytics-dashboard\images\audi.png", width=300)
    with col2:
        st.image(r"Car-analytics-dashboard\images\ferrari.png", width=220)
    with col3:
        st.image(r"Car-analytics-dashboard\images\ford.png", width=300)
    with col4:
        st.image(r"Car-analytics-dashboard\images\lamborghini.png", width=250)
    with col5:
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