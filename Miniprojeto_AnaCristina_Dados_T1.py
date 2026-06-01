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

#sprint 3
print(df.isnull().sum())
print(df.duplicated().sum())

df = df.drop_duplicates()
# Verifica valores únicos em CL_GENERO para identificar possíveis inconsistências
print(df['CL_GENERO'].unique())
print(df['CL_GENERO'].value_counts())
df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'Sem Categoria')
print(df.shape)
df.to_csv('df_limpo.csv', index=False)
print("\nArquivo df_limpo.csv salvo com sucesso!")

#sprint 4
print("Média:          ", df['CL_FHL'].mean())
print("Mediana:        ", df['CL_FHL'].median())
print("Desvio Padrão:  ", df['CL_FHL'].std())
print("Moda:           ", df['CL_FHL'].mode()[0])
print("Máximo:         ", df['CL_FHL'].max())
print("Mínimo:         ", df['CL_FHL'].min())
print("Contagem:       ", df['CL_FHL'].count())

print("\n--- Quartis ---")
print(df['CL_FHL'].quantile([0.25, 0.50, 0.75]))

#sprint 5
print(df.groupby('CL_GENERO')['CO_ID'].count().sort_values(ascending=False))
print(df.groupby('PR_CAT')['CO_ID'].count().sort_values(ascending=False))
print(df.groupby(['CL_GENERO', 'PR_CAT'])['CO_ID'].count().sort_values(ascending=False))