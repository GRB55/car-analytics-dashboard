import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
plt.style.use("dark_background")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "car-dataset-cleaned-2025.csv"

try:
    # Save the dataset in a dataframe
    df = pd.read_csv(DATA_PATH)
    # Streamlit App
    st.set_page_config(page_title="Exploration",
                       page_icon=":graph:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Title of the home page
    st.title("Exploratory Data Analysis",
             text_alignment="center")
    
    container = st.container(gap=None)
    with container:
        plt.figure(figsize=(9, 5))
        sns.countplot(data=df, y="brand", hue="brand", order=df['brand'].value_counts().index, palette="viridis")
        plt.title("Marcas con mayor cantidad de apariciones")
        plt.xlabel("")
        plt.ylabel("")
        plt.tight_layout()
        st.pyplot(plt)
        st.divider()
        
except FileNotFoundError:
    print("El archivo o la ruta no existen.")