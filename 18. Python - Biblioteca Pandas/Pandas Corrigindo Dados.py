import pandas as pd

df= pd.read_csv('dirtydata.csv')

# loc: location

# Define apenas 1 valor
# df.loc[7,'Duração'] = 45


# Define multiplos valores
# for x in df.index:
#     if df.loc[x, "Duração"] > 120:
#         df.loc[x, "Duração"]= 120

# Percore todas as linhas e REMOVE as linhas maiores que 120
for x in df.index:
    if df.loc[x, "Duração"] > 120:
        df.drop(x, inplace=True)




print(df.to_string())