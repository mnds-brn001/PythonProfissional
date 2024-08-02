import pandas as pd

data={
    "calorias": [420, 380, 390],
    "duraçao": [50, 40, 45]
}
# df= pd.DataFrame(data)
df= pd.DataFrame(data, index=["dia1", "dia2", "dia3"])
print(df)
print("####################")
print(df.loc["dia1"])

# print("####################")
# print(df.loc[0]) # Retorna uma Serie Pandas
# print("####################")
# print(df.loc[[0, 1]]) # Retorna um DataFrame Pandas
