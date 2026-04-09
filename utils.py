import pandas as pd
import streamlit as st
from pathlib import Path

@st.cache_data
def load_data():
    BASE_DIR = Path(__file__).resolve().parent
    DATA_PATH = BASE_DIR / "data" / "processed" / "cars_cleaned.csv"
    return pd.read_csv(DATA_PATH)