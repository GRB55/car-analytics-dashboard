import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
    st.title("Explorador",
             text_alignment="center")
    st.dataframe(df)
except FileNotFoundError:
    print("El archivo o la ruta no existen.")