import pandas as pd
from pathlib import Path

# Ruta de los datos
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw"
data = DATA_PATH / "Cars-Datasets-2025.csv"

# Cargar los datos en un marcode datos
df = pd.read_csv(data, encoding="utf-8", encoding_errors="ignore")

# Cambiar el nombre de las variables
columns = {"Company Names": "brand",
           "Cars Names": "model",
           "Engines": "engine",
           "CC/Battery Capacity": "battery_capacity",
           "HorsePower": "horse_power",
           "Total Speed": "top_speed",
           "Performance(0 - 100 )KM/H": "performance",
           "Cars Prices": "price",
           "Fuel Types": "fuel_type",
           "Seats": "seats",
           "Torque": "torque"}

df.rename(columns=columns, inplace=True)

# Limpieza de datos
df["battery_capacity"] = df["battery_capacity"].str.replace("cc", "")\
    .str.replace(",", "")\
        .str.strip()\
            .str.extract(r"(\d+(?:\.\d+)?)").astype(float)

df["horse_power"] = df["horse_power"].str.replace("hp", "")\
    .str.replace(",", "")\
        .str.strip()\
            .str.extract(r"(\d+(?:\.\d+)?)")

df["top_speed"] = df["top_speed"].str.replace("km/h", "")\
    .str.replace(",", "")\
        .str.strip()\
            .str.extract(r"(\d+(?:\.\d+)?)")

df["performance"] = df["performance"].str.replace("sec", "")\
    .str.strip()\
        .str.extract(r"(\d+(?:\.\d+)?)").astype(float)

df["torque"] = df["torque"].str.replace("Nm", "")\
    .str.strip()\
        .str.extract(r"(\d+(?:\.\d+)?)")

df["price"] = df["price"].str.replace("$", "")\
    .str.replace(",", "")\
        .str.strip()\
            .str.extract(r"(\d+(?:\.\d+)?)")
            
df["brand"] = df["brand"].str.lower()\
    .str.strip()
    
df["model"] = df["model"].str.lower()\
    .str.strip()

df["engine"] = df["engine"].str.lower()\
    .str.strip()

df["fuel_type"] = df["fuel_type"].str.lower()\
    .str.replace(r"[-/,()\s+]+", " ", regex=True)\
        .str.strip()

# Normalizamos los valores incorrectos
df.loc[df["seats"] == "2+2", "seats"] = 4
df.loc[df["seats"] == "212", "seats"] = 12
df.loc[df["seats"] == "29", "seats"] = 9
df.loc[df["seats"] == "78", "seats"] = 8
df.loc[df["seats"] == "26", "seats"] = 6
df.loc[df["seats"] == "27", "seats"] = 7
df.loc[df["seats"] == "215", "seats"] = 15

# Normalizamos los tipos de combustible
fuel_category_map = {
        "plug in hyrbrid": "hybrid",    
        "petrol": "petrol",
        "diesel": "diesel",
        "hybrid": "hybrid",
        "electric": "electric",
        "petrol diesel": "petrol",
        "plug in hybrid": "hybrid",
        "petrol awd": "petrol",
        "petrol hybrid": "hybrid",
        "hydrogen": "hydrogen",              
        "diesel petrol": 'diesel',
        "petrol ev": "petrol",
        "hybrid electric": "hybrid",
        "hybrid petrol": "hybrid",
        "cng petrol": "hybrid",
        "diesel hybrid": "hybrid",
        "hybrid gas electric": "hybrid",
        "gas hybrid": "hybrid",
        "hybrid plug in": "hybrid"
}
df["fuel_type"] = df["fuel_type"].map(fuel_category_map)

# Cambiar el tipo de datos al correcto
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["horse_power"] = pd.to_numeric(df["horse_power"], errors="coerce")
df["top_speed"] = pd.to_numeric(df["top_speed"], errors="coerce")
df["seats"] = pd.to_numeric(df["seats"], errors="coerce")
df["torque"] = pd.to_numeric(df["torque"], errors="coerce")

# Eliminar valores nulos y duplicados
df = df.dropna()
df = df.drop_duplicates()

# Exportar los datos limpios a un csv
export_path = BASE_DIR /"data" / "processed" / "car_cleaned.csv"
df.to_csv(export_path, index=False) 