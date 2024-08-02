import numpy as np

x= [1, 2, 3, 4]
y= [4, 5, 6, 7]

# z= []
# for i,j in zip(x,y):
#     z.append(i+j) # Somou ambas as listas e salvou em z
# Ou também, importando o numpy:
z= np.add(x,y)

print(z)

