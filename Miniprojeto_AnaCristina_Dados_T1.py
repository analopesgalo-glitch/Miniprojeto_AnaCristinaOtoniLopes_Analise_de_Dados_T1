import pandas as pd
import numpy as np

#sprint 1
df = pd.read_csv('Base Varejo.csv', sep=';')
print (df.shape)
print(df.dtypes)
print(df.head())