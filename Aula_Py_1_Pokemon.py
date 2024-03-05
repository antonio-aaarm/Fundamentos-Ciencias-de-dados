# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

#carregar dados

pokemon = pd.read_csv("C:/Users/20191enpro0140/Downloads/pokemon_data.csv")

#descrição dos dados

pokemon.describe()

#selecionando colunas especificas

pokemon_2 = pokemon[['Name', 'Type 1' , 'Type 2' ]]

#Filtrar por tipo do pokemon

pokemon_fogo = pokemon.loc[pokemon['Type 1']=="Fire"]

pokemon_fogo2 = pokemon[pokemon.iloc[:,2] == 'fire']

pokemon_fogo = pokemon.loc[(pokemon['Type 1']=="Fire") | (pokemon['Type 2']=="Fire") ]

#oredenção

pokemon_ataque = pokemon.sort_values('Attack',  ascending = False)

#estatistica de agregação

pokemon_agrupado = pokemon.groupby(['Type 1'])

pokemon_agrupado['Attack'].mean()
pokemon_agrupado['Attack'].std()
pokemon_agrupado['Attack'].median()
