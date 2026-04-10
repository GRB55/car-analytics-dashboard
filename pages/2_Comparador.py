import streamlit as st
import plotly.graph_objects as go
from utils import load_data

try:
    # Save the dataset in a dataframe
    df = load_data()
    df["car_name"] = df["brand"] + " " + df["model"]
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.title()
    # Streamlit App
    st.set_page_config(page_title="Comparador",
                       page_icon=":crossed_swords:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Title of the home page
    st.title("Comparador de autos",
             text_alignment="center")
    st.markdown("*Selecciona 2 autos que queres que sean comparados*", text_alignment="center")
    st.divider()
    opciones_autos = df["car_name"].unique()
    col1, col2 = st.columns(2)
    with col1:
        auto_seleccionado1 = st.selectbox(label="**PRIMER MODELO**", index=None, options=opciones_autos, placeholder="Selecciona un modelo")
        if auto_seleccionado1:
            filtrar_auto_seleccionado1 = df[df["car_name"] == auto_seleccionado1]
            st.metric(label="HP Promedio", 
                      value=str(round(filtrar_auto_seleccionado1["horse_power"].mean(), 2)) + " hp", 
                      border=True)
            st.info(f"""Tipo de Motor: {filtrar_auto_seleccionado1['engine'].values[0]}  
                        Combustible utilizado: {filtrar_auto_seleccionado1['fuel_type'].values[0]}""")
            st.metric(label="Velocidad Máxima", 
                      value=str(round(filtrar_auto_seleccionado1["top_speed"].max(), 2)) + " km/h", 
                      border=True)
            st.metric(label="Precio Promedio", 
                      value=filtrar_auto_seleccionado1["price"].mean(), 
                      border=True, format="dollar")
            st.metric(label="Cantidad Asientos",
                      value=filtrar_auto_seleccionado1["seats"].max(),
                      border=True)
    with col2:
        auto_seleccionado2 = st.selectbox(label="**SEGUNDO MODELO**", index=None, options=opciones_autos, placeholder="Selecciona un modelo")
        if auto_seleccionado2:
            filtrar_auto_seleccionado2 = df[df["car_name"] == auto_seleccionado2]
            st.metric(label="HP Promedio", 
                      value=str(round(filtrar_auto_seleccionado2["horse_power"].mean(), 2)) + " hp", 
                      border=True)
            st.info(f"""Tipo de Motor: {filtrar_auto_seleccionado2['engine'].values[0]}  
                        Combustible utilizado: {filtrar_auto_seleccionado2['fuel_type'].values[0]}""")
            st.metric(label="Velocidad Máxima", 
                      value=str(round(filtrar_auto_seleccionado2["top_speed"].max(), 2)) + " km/h", 
                      border=True)
            st.metric(label="Precio Promedio", 
                      value=filtrar_auto_seleccionado2["price"].mean(), 
                      border=True, format="dollar")
            st.metric(label="Cantidad Asientos",
                      value=filtrar_auto_seleccionado2["seats"].max(),
                      border=True)
            
except FileNotFoundError:
    print("El archivo o la ruta no existen.")