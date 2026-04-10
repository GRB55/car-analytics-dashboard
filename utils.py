import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path

def filtrar_outliers(df):
    df_filtrado = df.copy()
    for col in df.select_dtypes(include=np.number).columns:
        q1 = df_filtrado[col].quantile(0.25)
        q3 = df_filtrado[col].quantile(0.75)
        iqr = q3 - q1
        limite_inferior = q1 - iqr * 1.5
        limite_superior = q3 + iqr * 1.5
        df_filtrado = df_filtrado[(df_filtrado[col] >= limite_inferior) & (df_filtrado[col] <= limite_superior)]
    
    return df_filtrado

@st.cache_data
def load_data():
    BASE_DIR = Path(__file__).resolve().parent
    DATA_PATH = BASE_DIR / "data" / "processed" / "cars_cleaned.csv"
    return pd.read_csv(DATA_PATH)