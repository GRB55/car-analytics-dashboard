from pathlib import Path
import pandas as pd

def load_data():
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = BASE_DIR / "data" / "processed" / "car-dataset-cleaned-2025.csv"
    return pd.read_csv(data_path)