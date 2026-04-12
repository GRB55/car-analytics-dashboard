import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error

from sklearn.preprocessing import StandardScaler, OneHotEncoder, TargetEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from utils import load_data


# Instanciamos modelos predictivos
rf = RandomForestRegressor(random_state=42, n_jobs=-1)
lr = LinearRegression(n_jobs=-1)

try:
    # Guardar el dataset en un marco de datos
    df = load_data()    
    # Características y objetivo
    X = df.drop("price", axis=1)
    y = df["price"]
    # Conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Columnas
    cat_cols = [col for col in X.columns if X[col].dtype == "object"]
    num_cols = [col for col in X.columns if X[col].dtype != "object"]
    # Separar en baja y alta cardinalidad
    baja_card = [col for col in cat_cols if X[col].nunique() < 32]
    alta_card = [col for col in cat_cols if X[col].nunique() >= 32]
    # Preprocesamiento de datos
    preprocesador = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("onehot", OneHotEncoder(), baja_card),
            ("target", TargetEncoder(), alta_card)
        ]
    )
    # Pipeline rf
    pipeline_rf = Pipeline(
        steps=[
            ("preprocessor", preprocesador),
            ("model", rf)
        ]
    )
    # Entrenamiento rf
    pipeline_rf.fit(X_train, y_train)
    # Predicciones rf
    rf_y_pred = pipeline_rf.predict(X_test)
    # Métricas
    rf_mse = mean_squared_error(y_test, rf_y_pred)
    rf_rmse = root_mean_squared_error(y_test, rf_y_pred)
    rf_r2 = r2_score(y_test, rf_y_pred)
except FileNotFoundError:
    print("El archivo o la ruta no existen.")