import pandas as pd
import numpy as np

#sprint 1
df = pd.read_csv('Base Varejo.csv', sep=';')
print (df.shape)
print(df.dtypes)
print(df.head())

#sprint 2
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
df = df.drop(columns=['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'])
print (df.dtypes)