from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# x= random.exponential(scale=2, size=(2, 3))


x= random.exponential(size=1000)
sns.distplot(x, hist=False)

plt.show()
#print(x)