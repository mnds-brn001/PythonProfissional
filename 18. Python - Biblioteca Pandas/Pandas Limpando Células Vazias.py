import pandas as pd

df= pd.read_csv('dirtydata.csv')
# print(df.to_string())


# new_df= df.dropna() # Remoçao das células vazias
# new_df= df.dropna(inplace=True) # Altera o DF original com o inplace=True
# print(df.to_string())

# df.fillna(130, inplace=True)
# df["Calorias"].fillna(130, inplace=True)
# print(df.to_string())

# Substituindo os valores nulos pela Media
# x= df["Calorias"].mean() # Soma de todos os valores dividido pelo nº de valores
# df["Calorias"].fillna(x, inplace=True)
# print(df.to_string())

# Substituindo os valores nulos pela Mediana
# x= df["Calorias"].median() # Calcula o valor no meio e classifica os valores em ordem crescente
# df["Calorias"].fillna(x, inplace=True)
# print(df.to_string())

# Retorna o valor que aparece com mais frequência
x= df["Calorias"].mode()[0]
df["Calorias"].fillna(x, inplace=True)
print(df.to_string())
