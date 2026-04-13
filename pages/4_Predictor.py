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
    cat_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]
    num_cols = [col for col in X_train.columns if X_train[col].dtype != "object"]
    # Separar en baja y alta cardinalidad
    baja_card = [col for col in cat_cols if X_train[col].nunique() < 32]
    alta_card = [col for col in cat_cols if X_train[col].nunique() >= 32]
    # Preprocesamiento de datos
    preprocesador_rf = ColumnTransformer(
        transformers=[
            ("num", "passthrough", num_cols),
            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False), baja_card),
            ("target", TargetEncoder(random_state=42), alta_card)
        ]
    )
    # Pipeline rf
    pipeline_rf = Pipeline(
        steps=[
            ("preprocessor", preprocesador_rf),
            ("model", rf)
        ]
    )
    # Entrenamiento rf
    pipeline_rf.fit(X_train, y_train)
    # Predicciones rf
    rf_y_pred = pipeline_rf.predict(X_test)
    # Métricas rf
    rf_mse = mean_squared_error(y_test, rf_y_pred)
    rf_rmse = root_mean_squared_error(y_test, rf_y_pred)
    rf_r2 = r2_score(y_test, rf_y_pred)
    # Preprocesamiento de datos
    preprocesador_lr = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False), baja_card),
            ("target", TargetEncoder(random_state=42), alta_card)
        ]
    )
    # Pipeline lr
    pipeline_lr = Pipeline(
        steps=[
            ("preprocessor", preprocesador_lr),
            ("model", lr)
        ]
    )
    # Entrenamiento lr
    pipeline_lr.fit(X_train, y_train)
    # Predicciones lr
    lr_y_pred = pipeline_lr.predict(X_test)
    # Métricas lr
    lr_mse = mean_squared_error(y_test, lr_y_pred)
    lr_rmse = root_mean_squared_error(y_test, lr_y_pred)
    lr_r2 = r2_score(y_test, lr_y_pred)
    # Almacenamos los resultados en un marco de datos
    resultados = pd.DataFrame({
        "R2": [rf_r2, lr_r2],
        "MSE": [rf_mse, lr_mse],
        "RMSE": [rf_rmse, lr_rmse]
    }, index=["Random Forest", "Regresión Lineal"])
    # Streamlit page
    st.set_page_config(page_title="Predictor de Precio",
                       page_icon=":robot:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Titulo de la home page
    st.title("Predictor de Precios",
             text_alignment="center")
    st.dataframe(resultados)
except FileNotFoundError:
    print("El archivo o la ruta no existen.")