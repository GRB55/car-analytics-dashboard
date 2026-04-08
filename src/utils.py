import pandas as pd
from pathlib import Path

def load_data():
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_PATH = BASE_DIR / "data" / "processed" / "cars_cleaned.csv"
    return pd.read_csv(DATA_PATH)