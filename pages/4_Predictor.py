import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder, TargetEncoder
from utils import load_data


# Instanciamos modelos predictivos
rf = RandomForestRegressor(random_state=42, n_jobs=-1)
lr = LinearRegression(n_jobs=-1)

# Herramientas para el preprocesamiento de datos
scaler = StandardScaler()
oh_encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
tgt_encoder = TargetEncoder()

try:
    # Guardar el dataset en un marco de datos
    df = load_data()    
    # Características y objetivo
    X = df.drop("price", axis=1)
    y = df["price"]
    # Conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Preprocesamiento de datos
except FileNotFoundError:
    print("El archivo o la ruta no existen.")