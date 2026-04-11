import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder, TargetEncoder
from utils import load_data

# frecuency encoder -> frecuencia de aparicion de la categoria
# target encoding -> reemplazar la categoria por el promedio del target
# Página 4 — 🤖 Predictor de Precio
# Tu misión: formulario donde el usuario ingresa specs y se predice el precio.
# Investigá:

# st.form + st.form_submit_button (importante: evita reruns en cada widget)
# Entrenás un modelo simple (RandomForestRegressor de sklearn) al cargar la página
# st.spinner mientras "predice"
# st.success / st.error para mostrar el resultado
# Bonus: st.expander para mostrar la importancia de cada feature

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
    # Caracteristicas y objetivo