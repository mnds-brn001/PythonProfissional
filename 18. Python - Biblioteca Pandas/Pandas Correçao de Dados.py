import pandas as pd

df= pd.read_csv('data.csv')


# Corr

print(df.to_string())
print(df.corr())