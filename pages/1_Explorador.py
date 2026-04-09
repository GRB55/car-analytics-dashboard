import streamlit as st
from utils import load_data

try:
    # Save the dataset in a dataframe
    df = load_data()
    # Streamlit App
    st.set_page_config(page_title="Explorador",
                       page_icon=":mag_right:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Title of the home page
    st.title("Explorador de Datos",
             text_alignment="center")
    st.divider()
    st.subheader("Conjunto de Datos Original")
    st.dataframe(df, use_container_width=True)
    with st.sidebar:
        brand_filter = st.multiselect(label="Selecciona la marca",
                                      options=df["brand"].unique(),
                                      default=None)
        fuel_type_filter = st.multiselect(label="Selecciona el tipo de combustible",
                                          options=df["fuel_type"].unique(),
                                          default=None)
        max_price = st.slider(label="Rango de precios",
                              min_value=df["price"].min(),
                              max_value=df["price"].max(),
                              value=df["price"].max(),
                              format="dollar")
        max_horse_power = st.slider(label="Caballos de fuerza",
                                    min_value=df["horse_power"].min(),
                                    max_value=df["horse_power"].max(),
                                    value=df["horse_power"].max())
        
    filtered_df = df[((df["brand"].isin(brand_filter)) &
                         (df["fuel_type"].isin(fuel_type_filter)) &
                         (df["price"] <= max_price) &
                         (df["horse_power"] <= max_horse_power))]
    st.divider()
    st.subheader("Conjunto de Datos filtrado")
    st.dataframe(filtered_df)
    new_file = filtered_df.to_csv()
    st.download_button(label="Descargar el conjunto de datos filtrado",
                       data=new_file,
                       file_name="data.csv",
                       mime="text/csv",
                       icon=":material/download:")
except FileNotFoundError:
    print("El archivo o la ruta no existen.")