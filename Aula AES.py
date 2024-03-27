# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import SimpleExpSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns

data = pd.read_csv("C:/Users/20191enpro0140/Downloads/st_ds8_birth.csv", parse_dates= [0], index_col= 0)

grafico = data.plot()
grafico.set_xlabel("Dia")
grafico.set_ylabel("Nascimento")

#####
#Amortecimento Exponencial Simples
####

treino = data.iloc[:292,]
teste = data.iloc[292:,]

# Usando os dados de treino para obter o valor de alpha

modelo_aes = SimpleExpSmoothing(treino).fit()

# ver qual foi o alpha otimizado

modelo_aes.summary()

#usando o alfa para fazer previsões na amostra de teste

modelo_aes_teste = SimpleExpSmoothing(teste).fit(smoothing_level=0.0600966)

#valores previstos na amostra de teste

prev_aes_teste = modelo_aes_teste.fittedvalues

#calculando o MAPE


MAPE = (np.mean(np.abs((prev_aes_teste - teste.squeeze())/teste.squeeze())))*100

grafico = teste.squeeze().plot()
grafico.plot(prev_aes_teste)
grafico.legend(['dados de teste', 'Previsões'])
