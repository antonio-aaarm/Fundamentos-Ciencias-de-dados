# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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

pokemon.head()
pokemon.tail()

# 800 casos 12 variaveis

#selecionando colunas especificas

pokemon_defesa_tipo = pokemon[['Name', 'Type 1' , 'Type 2' , 'Defense', 'Sp. Def']]

pokemon_defesa_tipo = pokemon_defesa_tipo.sort_values('Defense',  ascending = False)

#estatistica de agregação

pokemon_agrupado = pokemon.groupby(['Type 1'])

pokemon_agrupado['Type 1'].count()
pokemon_agrupado['Type 2'].count()

pokemon['Type 1'].value_counts() + pokemon['Type 2'].value_counts()

pokemon['ataque_defesa'] = pokemon['Attack'] / pokemon['Defense']


pokemon_agrupado['Defense'].mean()
pokemon_agrupado['Defense'].std()











