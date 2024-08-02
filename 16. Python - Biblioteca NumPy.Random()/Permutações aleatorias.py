import numpy as np
from numpy import random

arr= np.array([1, 2, 3, 4, 5])

#random.shuffle(arr) # Altera o array original
newarr= random.permutation(arr)

print(arr)
print(newarr)