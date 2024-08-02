# Multiplicação
import numpy as np

arr= np.array([1,2,3,4])
arr2= np.array([5,6,7,8])

# x= np.prod(arr)
# x= np.prod([arr, arr2])
# x= np.prod([arr, arr2], axis=1) # Multiplicação de todos os valores em matrizes separadas

# x= np.cumprod([arr, arr2], axis=1)

x= np.cumprod(arr)
newarr=np.cumprod(arr2)
print(x)
print(newarr)