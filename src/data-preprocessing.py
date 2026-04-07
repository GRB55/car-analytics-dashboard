import pandas as pd

data = r"Cars Datasets 2025.csv"

df = pd.read_csv(data, encoding="utf-8", encoding_errors="ignore")

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

for i in range(len(df["price"])):
    if len(df["price"].str.strip()[i]) > 10:
        print(df["price"][i])

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

df["price"] = pd.to_numeric(df["price"], errors="coerce")

df["battery_capacity"] = pd.to_numeric(df["battery_capacity"], errors="coerce")

df["horse_power"] = pd.to_numeric(df["horse_power"], errors="coerce")

df["max_speed"] = pd.to_numeric(df["max_speed"], errors="coerce")

df["performance_0_100"] = pd.to_numeric(df["performance_0_100"], errors="coerce")

df = df.dropna()

df.to_csv("car-dataset-cleaned-2025.csv", index=False)