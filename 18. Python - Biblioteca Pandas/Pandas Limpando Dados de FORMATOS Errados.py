import pandas as pd

df= pd.read_csv('dirtydata.csv')

df["Data"] = pd.to_datetime(df["Data"])

df.dropna(subset=['Data'], inplace=True)

print(df.to_string())
