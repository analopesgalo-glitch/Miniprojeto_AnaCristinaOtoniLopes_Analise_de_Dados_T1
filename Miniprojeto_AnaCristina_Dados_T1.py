import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

#sprint 6
# --- CONCLUSÕES E INSIGHTS ---

print("=" * 60)
print("CONCLUSÕES DA ANÁLISE EXPLORATÓRIA - BASE VAREJO")
print("=" * 60)

print("""
1. QUALIDADE DA BASE
   A base original continha 830.000 registros e 14 colunas.
   Após a limpeza, ficamos com 733.447 registros e 10 colunas.
   Foram removidas 96.553 linhas duplicadas (11,6% da base)
   e 4 colunas completamente vazias (Unnamed).

2. CATEGORIAS INVÁLIDAS
   Foram encontrados 3.228 registros com categoria '#N/D'
   na coluna PR_CAT. Esses valores foram tratados como
   'Sem Categoria' por não representarem dados válidos.

3. PERFIL DE COMPRAS POR GÊNERO
   Mulheres (F) realizaram 382.427 compras contra 351.020
   dos homens (M), representando 52% do total de compras.
   Mulheres lideram em todas as categorias de produtos.

4. CATEGORIAS MAIS VENDIDAS
   ALIMENTOS lidera com 384.197 compras (52% do total),
   seguida de HIGIENE (137.702) e LIMPEZA (128.632).
   ACESSORIOS é a categoria menos vendida com 12.871 compras.

5. PERFIL DE FILHOS DOS CLIENTES
   A maioria dos clientes não tem filhos (moda e mediana = 0).
   A média de 1,14 filhos indica que uma minoria com muitos
   filhos eleva a média. O máximo registrado foi 4 filhos.

6. PROBLEMAS REMANESCENTES
   Os 3.228 registros classificados como 'Sem Categoria'
   merecem investigação futura para identificar o produto
   correto. A origem do '#N/D' pode indicar falha no
   sistema de origem dos dados.
""")

# GRÁFICO: COMPARAÇÃO DE GÊNERO NAS CATEGORIAS ESTRATÉGICAS

# Filtra apenas as categorias onde a diferença entre gêneros é menor
categorias_foco = ['BEBIDAS', 'PET', 'ACESSORIOS']
df_foco = df[df['PR_CAT'].isin(categorias_foco)]

# Prepara os dados agrupados para o gráfico
df_grafico = df_foco.groupby(['PR_CAT', 'CL_GENERO'])['CO_ID'].count().reset_index()
df_grafico.columns = ['Categoria', 'Genero', 'Compras']

# Cria o gráfico de barras comparativo
plt.figure(figsize=(10, 6))
sns.barplot(data=df_grafico, x='Categoria', y='Compras', hue='Genero')
plt.title('Categorias com maior potencial de crescimento masculino')
plt.xlabel('Categoria')
plt.ylabel('Número de Compras')
plt.legend(title='Gênero')
plt.tight_layout()
plt.savefig('grafico_genero_categorias.png')
plt.show()
print("Gráfico salvo como grafico_genero_categorias.png")

# CONCLUSÃO

print("""
7. RECOMENDAÇÃO ESTRATÉGICA PARA MARKETING
   Nas categorias BEBIDAS, PET e ACESSORIOS, a diferença
   entre compras femininas e masculinas é pequena:
   - BEBIDAS:    F=19.764  M=18.500  (diferença de 1.264)
   - PET:        F=14.809  M=13.744  (diferença de 1.065)
   - ACESSORIOS: F=6.839   M=6.032   (diferença de 807)
   
   Recomenda-se aumentar investimento em campanhas
   direcionadas ao público masculino nessas categorias,
   onde o potencial de crescimento é maior com menor
   esforço comparativo.
""")