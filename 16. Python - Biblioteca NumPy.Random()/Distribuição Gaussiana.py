from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#x= random.normal(size=(2, 3)) # 2-D com 3 Elementos
#x= random.normal(loc=1, scale=2, size=(2, 3))

x= random.normal(size= 1000)
sns.distplot(x, hist=False)
print(x)
