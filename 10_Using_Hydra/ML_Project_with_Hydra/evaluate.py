#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Script de Avaliação
===================
Aqui avaliamos nossas previsões com a métrica
MSE, a qual se usa em Regressão Linear.
"""
from sklearn.metrics import mean_squared_error

def evaluate_model(model, X_test, y_test):
    # Fazer previsões no conjunto de teste:
    predictions = model.predict(X_test)
    
    # Calcular o erro médio quadrático:
    mse = mean_squared_error(y_test, predictions)
    
    return mse
