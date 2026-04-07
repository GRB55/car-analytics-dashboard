import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path.cwd().parent
DATA_PATH = BASE_DIR / "data" / "processed"
FILE_PATH = DATA_PATH / "car-dataset-cleaned-2025.csv"

df = pd.read_csv(FILE_PATH)

df