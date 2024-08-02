# Distribuição discreta, é aplicada em casos de experimentos repetidos, onde existem dois possíveis resultados: cara ou coroa, sucesso ou fracasso, item defeituoso ou item não defeituoso 
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x= random.binomial(n=10, p=0.5, size=10)
#sns.displot(x, kde=True)

a= random.normal(loc=50, scale=5, size=1000)
sns.distplot(a, hist=False, label="normal")

b= random.binomial(n=100, p=0.5, size=1000)
sns.distplot(b, hist=False, label="binomial")

plt.show()

#print(x)