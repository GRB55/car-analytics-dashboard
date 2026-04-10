import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from utils import load_data

# frecuency encoder -> frecuencia de aparicion de la categoria
# target encoding -> reemplazar la categoria por el promedio del target