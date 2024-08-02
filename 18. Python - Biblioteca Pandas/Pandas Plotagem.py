import pandas as pd
import matplotlib.pyplot as plt


df= pd.read_csv('data.csv')


# kind Scatter
# df.plot()
# df.plot(
#     kind='scatter',
#     x='Duração',
#     y='Calorias')

# df.plot(
#     kind='scatter',
#     x='Duração',
#     y='Maxpulso')


df["Duração"].plot(
    kind='hist'
    )

plt.show()

#print(df.to_string())
