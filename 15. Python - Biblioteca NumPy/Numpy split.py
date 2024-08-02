import numpy as np

arr = np.array([1,2,3,4,5,6,7])

# print(arr[1:5])
# print(arr[4:]) # Inicio no indice 4 até o final
# print(arr[:3]) # Do começo até o indice 3
# print(arr[-3:-1])
# print(arr[1:5:2]) # Inicia na indice 1 e de 2 em 2 vai até o indice 5
# print(arr[::3]) # Conta todo o array ao passo de 3

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1, 1:4]) # Primeiro valor é sobre o indice do array, e o segundo o metodo de fatiamento

print(arr[0:2, 2]) # Fatia dos dois elementos, o indice 2
print(arr[0:2, 1:4]) # Fatia dos dois elementos, os indices de 1 a 4