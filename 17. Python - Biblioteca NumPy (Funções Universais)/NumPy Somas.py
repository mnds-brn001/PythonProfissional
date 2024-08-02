import numpy as np


arr1= np.array([1, 2, 3])
arr2= np.array([1, 2, 3])

# Soma os arrays indice a indice e devolve uma lista
newarr= np.add(arr1, arr2)
print(newarr)

# Soma todos os valores do array e retorna um único valor.
newarr=np.sum([arr1, arr2])
print(newarr)

#Soma de todos os valores em cada array separadamente e junta em uma lista
newarr= np.sum([arr1, arr2], axis=1)
print(newarr)

# Soma parcial
newarr= np.cumsum([arr1])
print(newarr)

