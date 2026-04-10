import streamlit as st
import plotly.express as px
from utils import load_data, filtrar_outliers

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
        outliers_on = st.toggle(label="Mostrar valores atípicos")
        if outliers_on:
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
                            color="brand", size="horse_power", symbol="brand",
                            color_discrete_sequence=px.colors.qualitative.Light24,
                            category_orders=dict(brand=sorted(df["brand"].unique())))
            fig1.update_layout(
                xaxis_title_text = "HP",
                yaxis_title_text = "Precio",
                legend_title_text = "Marca",
                legend = dict(font=dict(size=11), itemsizing="constant")
            )
            st.plotly_chart(fig1)
        else:
            df_filtrado = filtrar_outliers(df)
            marcas_ordenadas = df_filtrado.groupby("brand")["price"].mean().sort_values(ascending=False).index
            fig = px.histogram(data_frame=df_filtrado, 
                            x="brand", y="price",
                            color_discrete_sequence=['indianred'], 
                            histfunc="avg", category_orders=dict(brand = marcas_ordenadas))
            fig.update_layout(
                xaxis_title_text = "Marca",
                yaxis_title_text = "Precio Promedio"
            )
            st.plotly_chart(fig)
            fig1 = px.scatter(data_frame=df_filtrado,
                            x="horse_power", y="price",
                            color="brand", size="horse_power", symbol="brand",
                            color_discrete_sequence=px.colors.qualitative.Light24,
                            category_orders=dict(brand=sorted(df_filtrado["brand"].unique())))
            fig1.update_layout(
                xaxis_title_text = "HP",
                yaxis_title_text = "Precio",
                legend_title_text = "Marca",
                legend = dict(font=dict(size=11), itemsizing="constant")
            )
            st.plotly_chart(fig1)
    with tab2:
        outliers_on = st.toggle(label="Mostrar valores atípicos")
        if outliers_on:
            combustible_ordenados = df.groupby("fuel_type")["price"].mean().sort_values(ascending=False).index
            fig = px.histogram(data_frame=df, 
                            x="fuel_type", y="price", opacity=0.75,
                            color_discrete_sequence=['tomato'], 
                            histfunc="avg", category_orders=dict(fuel_type = combustible_ordenados))
            fig.update_layout(
                xaxis_title_text = "Combustible",
                yaxis_title_text = "Precio Promedio"
            )
            st.plotly_chart(fig)
            fig1 = px.scatter(data_frame=df,
                            x="horse_power", y="price", symbol="fuel_type",
                            color="fuel_type", size="horse_power",
                            color_discrete_sequence=px.colors.qualitative.Alphabet,
                            category_orders=dict(fuel_type=sorted(df["fuel_type"].unique())))
            fig1.update_layout(
                xaxis_title_text = "HP",
                yaxis_title_text = "Precio",
                legend_title_text = "Combustible",
                legend = dict(font=dict(size=11), itemsizing="constant")
            )
            st.plotly_chart(fig1)
        else:
            df_filtrado = filtrar_outliers(df)
            marcas_ordenadas = df_filtrado.groupby("brand")["price"].mean().sort_values(ascending=False).index
            fig = px.histogram(data_frame=df_filtrado, 
                            x="brand", y="price",
                            color_discrete_sequence=['indianred'], 
                            histfunc="avg", category_orders=dict(brand = marcas_ordenadas))
            fig.update_layout(
                xaxis_title_text = "Marca",
                yaxis_title_text = "Precio Promedio"
            )
            st.plotly_chart(fig)
            fig1 = px.scatter(data_frame=df_filtrado,
                            x="horse_power", y="price",
                            color="brand", size="horse_power", symbol="brand",
                            color_discrete_sequence=px.colors.qualitative.Light24,
                            category_orders=dict(brand=sorted(df_filtrado["brand"].unique())))
            fig1.update_layout(
                xaxis_title_text = "HP",
                yaxis_title_text = "Precio",
                legend_title_text = "Marca",
                legend = dict(font=dict(size=11), itemsizing="constant")
            )
            st.plotly_chart(fig1)
    with tab3:
        corr = df.corr(numeric_only=True)
        cor_fig = px.imshow(corr, text_auto=True, width=1200, height=600)
        st.plotly_chart(cor_fig)
except FileNotFoundError:
    print("El archivo o la ruta no existen.")