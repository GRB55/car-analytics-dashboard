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
    st.header("Performance de los modelos")
    st.dataframe(resultados)
    st.success(f"Mejor modelo: {resultados.iloc[0]['Modelo']}")
    st.error(f"Peor modelo: {resultados.iloc[5]['Modelo']}")
    with st.form("Introduce los datos para predecir el valor de un auto:"):
        modelo_pred = st.selectbox("Modelo predictivo", options=modelos.keys())
        marca_auto = st.selectbox("Marca de auto", options=df["brand"].unique())
        modelo_auto = st.selectbox("Modelo de auto", options=df["model"].unique())
        motor_auto = st.selectbox("Motor de auto", options=df["engine"].unique())
        combustible = st.selectbox("Combustible del auto", options=df["fuel_type"].unique())
        bateria = st.number_input("Capacidad de la bateria", min_value=0.0, max_value=df["battery_capacity"].max())
        hp = st.number_input(label="HP", min_value=0, max_value=df["horse_power"].max())
        velocidad_max = st.number_input(label="Velocidad maxima (km/h)", min_value=0, max_value=df["top_speed"].max())
        performance = st.number_input(label="Performance", min_value=0.0, max_value=df["performance"].max())
        asientos = st.number_input(label="Cantidad de asientos", min_value=0, max_value=df["seats"].max())
        torque = st.number_input(label="Capacidad de torque", min_value=0.0, max_value=df["torque"].max())
        enviar = st.form_submit_button("Entrenar")
        if enviar:
            with st.spinner(f"Entrenando {modelo_pred}", show_time=True):
                new_data = pd.DataFrame([{
                    "brand": marca_auto,
                    "model": modelo_auto,
                    "engine": motor_auto,
                    "battery_capacity": bateria,
                    "horse_power": hp,
                    "top_speed": velocidad_max,
                    "performance": performance,
                    "fuel_type": combustible,
                    "seats": asientos,
                    "torque": torque
                }])
                pipeline = Pipeline(
                    steps=[
                        ("preprocessor", clone(preprocesador)),
                        ("model", modelos[modelo_pred])
                    ]
                )
                # Entrenamiento
                pipeline.fit(X_train, y_train)
                # Predicciones
                y_pred = pipeline.predict(new_data)
                # Precio predicho
                st.success(f"Precio predicho: ${y_pred}")
except FileNotFoundError:
    print("El archivo o la ruta no existen.")