import numpy as np

arr= np.array([1,2,3,4,5,4,4])

# x= np.where(arr == 4)
# x= np.where(arr%2 == 0) # devolve os indices divisiveis por 2
x= np.where(arr%2 == 1) # Retorna os indices divisiveis por impares



print(x)