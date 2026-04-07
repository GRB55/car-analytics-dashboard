import pandas as pd
from pathlib import Path

# Data file path
BASE_DIR = Path.cwd().parent
DATA_PATH = BASE_DIR / "data" / "raw"
FILE_PATH = "Cars Datasets 2025.csv"
data = DATA_PATH / FILE_PATH

# Load the data in a dataframe
df = pd.read_csv(data, encoding="utf-8", encoding_errors="ignore")

# Change the variables names
columns = {"Company Names": "brand",
           "Cars Names": "model",
           "Engines": "engine",
           "CC/Battery Capacity": "battery_capacity",
           "HorsePower": "horse_power",
           "Total Speed": "max_speed",
           "Performance(0 - 100 )KM/H": "performance_0_100",
           "Cars Prices": "price",
           "Fuel Types": "fuel",
           "Seats": "seats",
           "Torque": "torque"}

df.rename(columns=columns, inplace=True)

# What chars were used to give a range of values
for i in range(len(df["price"])):
    if len(df["price"].str.strip()[i]) > 10:
        print(df["price"][i])

# Data cleaning
df["battery_capacity"] = df["battery_capacity"].str.replace("cc", "")\
    .str.replace(",", "")\
        .str.strip()\
            .str.split(r"-|/| ", n=1, expand=True)[0]

df["horse_power"] = df["horse_power"].str.replace("hp", "")\
    .str.replace(",", "")\
        .str.strip()\
            .str.split(r"-|/| ", n=1, expand=True)[0]

df["max_speed"] = df["max_speed"].str.replace("km/h", "")\
    .str.replace(",", "")\
        .str.strip()\
            .str.split(r"-|/| ", n=1, expand=True)[0]

df["performance_0_100"] = df["performance_0_100"].str.replace("sec", "")\
    .str.strip()\
        .str.split(r"-|/| ", n=1, expand=True)[0]

df["torque"] = df["torque"].str.replace("Nm", "")\
    .str.strip()\
        .str.split(r"-|/| ", n=1, expand=True)[0]

df["price"] = df["price"].str.replace("$", "")\
    .str.replace(",", "")\
        .str.strip()\
            .str.split(r"-|/| ", n=1, expand=True)[0]

df.loc[df["engine"].str.lower() == "electric motor", "engine"] = df.loc[df["engine"].str.lower() == "electric motor", "engine"].str.extract(r"(\d+(?:\.\d+)?)").astype(float)

# Change the data type into the correct one
df["price"] = pd.to_numeric(df["price"], errors="coerce")

df["battery_capacity"] = pd.to_numeric(df["battery_capacity"], errors="coerce")

df["horse_power"] = pd.to_numeric(df["horse_power"], errors="coerce")

df["max_speed"] = pd.to_numeric(df["max_speed"], errors="coerce")

df["performance_0_100"] = pd.to_numeric(df["performance_0_100"], errors="coerce")

df = df.dropna()

# Export the clean data into a csv
# export_path = BASE_DIR /"data" / "processed" / "car-dataset-cleaned-2025.csv"
# df.to_csv(export_path, index=False) 