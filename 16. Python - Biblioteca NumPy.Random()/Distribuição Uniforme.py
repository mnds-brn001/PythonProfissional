from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# x= random.uniform(size=(2, 3))

x= random.uniform(low=-1, high=0, size=1000)
sns.distplot(x, hist=False)

plt.show()
print(x)