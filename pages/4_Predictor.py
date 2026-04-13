import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, HistGradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, root_mean_squared_error

from sklearn.base import clone
from sklearn.preprocessing import StandardScaler, OneHotEncoder, TargetEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from utils import load_data, filtrar_outliers


# Instanciamos modelos predictivos
rf = RandomForestRegressor(random_state=42, n_jobs=-1)

try:
    # Guardar el dataset en un marco de datos
    df = load_data()
    df_sin_outliers = filtrar_outliers(df)
    # Características y objetivo
    X = df_sin_outliers.drop("price", axis=1)
    y = df_sin_outliers["price"]
    # Conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Columnas
    cat_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]
    num_cols = [col for col in X_train.columns if X_train[col].dtype != "object"]
    # Separar en baja y alta cardinalidad
    baja_card = [col for col in cat_cols if X_train[col].nunique() < 32]
    alta_card = [col for col in cat_cols if X_train[col].nunique() >= 32]
    # Preprocesamiento de datos
    preprocesador = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False), baja_card),
            ("target", TargetEncoder(random_state=42), alta_card)
        ]
    )
    modelos = {
        "XGBoost": XGBRegressor(n_estimators=300, learning_rate=0.05, random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=300, random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=300, learning_rate=0.05, random_state=42),
        "Árbol de Decisión": DecisionTreeRegressor(random_state=42),
        "Regresión Lineal": LinearRegression(),
        "Hist Gradient Boosting": HistGradientBoostingRegressor(learning_rate=0.05, random_state=42)
    }
    resultado = []
    for name, model in modelos.items():
        print(f"Entrenando {name}")
        pipeline = Pipeline(
            steps=[
                ("preprocessor", clone(preprocesador)),
                ("model", model)
            ]
        )
        # Entrenamiento
        pipeline.fit(X_train, y_train)
        # Predicciones
        y_pred = pipeline.predict(X_test)
        # Metricas
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = root_mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        # Guardamos resultados
        resultado.append([name, mae, mse, rmse, r2])
    resultados = pd.DataFrame(resultado, columns=["Modelo", "MAE", "MSE", "RMSE", "R2"])
    resultados = resultados.sort_values("R2", ascending=False)
    # Streamlit page
    st.set_page_config(page_title="Predictor de Precio",
                       page_icon=":robot:",
                       layout="wide",
                       initial_sidebar_state="expanded")
    # Titulo de la home page
    st.title("Predictor de Precios",
             text_alignment="center")
    st.dataframe(resultados)
    st.success(f"Mejor modelo: {resultados.iloc[0]['Modelo']}")
except FileNotFoundError:
    print("El archivo o la ruta no existen.")