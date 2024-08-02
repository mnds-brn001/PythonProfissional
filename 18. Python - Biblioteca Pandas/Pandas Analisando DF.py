import pandas as pd

df= pd.read_csv("data.csv")
# print(df.head(10))
# print(df.head()) # Por padrão mostra apenas 5 linhas

# print(df.tail(10))
# print(df.tail()) # Por padrão mostra apenas 5 linhas

print(df.info())