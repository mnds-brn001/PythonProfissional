import pandas as pd

df= pd.read_csv('dirtydata.csv')

# Devolve um valor booleano para linhas duplicadas
print(df.duplicated())

df.drop_duplicates(inplace=True) # Linha 12 removida

print(df.to_string())

