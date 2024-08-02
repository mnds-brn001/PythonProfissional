from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# x= random.logistic(loc=1, scale=2, size=(2,3))
# sns.distplot(x, hist=False)

a= random.normal(scale=2, size=1000)
sns.distplot(a, hist=False, label='normal')

b= random.logistic(size=1000)
sns.distplot(b, hist=False, label='logistica')


#print(x)
plt.show()