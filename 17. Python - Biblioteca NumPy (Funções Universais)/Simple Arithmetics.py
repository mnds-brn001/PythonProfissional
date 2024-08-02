import numpy as np

arr1= np.array([10, 11, 12, 13, 14 ,15])
arr2= np.array([20, 21 ,22, 23, 24, 25])

# Adição
newarr= np.add(arr1, arr2)
print(newarr)

# Subtração
newarr= np.subtract(arr1, arr2)
print(newarr)

# Multiplicação
newarr= np.multiply(arr1, arr2)
print(newarr)

# Divisão
newarr= np.divide(arr1, arr2)
print(newarr)

# Potência
newarr= np.power(arr1, arr2)
print(newarr)

# Resto da Divisão
newarr= np.mod(arr1, arr2)
print(newarr)
newarr= np.remainder(arr1, arr2)
print(newarr)

# Quociente e Mod 1º| Array:Quociente 2º Array:Mod
newarr= np.divmod(arr1, arr2)
print(newarr)

# Valores Absolutos
newarr= np.absolute(arr1, arr2)
print(newarr)

arr= np.array([-1, -2, 1, 2, 3, 4])
arr= np.absolute(arr)
print(arr)

print("####################################")

x= np.array([10, 11, 12, 13, 14 ,15
])
y= np.array([20, 21 ,22, 23, 24, 25])

z= np.add(x,y, where=x>12)
print(z)