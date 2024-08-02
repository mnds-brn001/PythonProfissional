# Processamento de sinais
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# x= random.rayleigh(scale=2, size=(2,3))
# print(x)

x= random.rayleigh(size=1000)
sns.displot(x)

plt.show()