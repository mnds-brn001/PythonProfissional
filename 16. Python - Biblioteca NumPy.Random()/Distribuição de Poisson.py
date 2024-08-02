#A distribuição de Poisson descreve resultados de experiências nos quais contamos acontecimentos que ocorrem aleatoriamente mas a uma taxa média definida. Por exemplo: as contagens de um decaimento radioactivo ou o nº de bebés que nasce por mês num determinado hospital.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# x= random.poisson(lam=2, size=1000)
# sns.distplot(x, kde=False)

# a= random.normal(loc=50, scale=7, size=1000)
# sns.distplot(a, hist=False, label='normal')

a= random.binomial(n=100,p=0.1, size=1000)
sns.distplot(a, hist=False, label='binomial')


b= random.poisson(lam=10, size=1000)
sns.distplot(b, hist=False, label='poisson')

plt.show()
#print(x)