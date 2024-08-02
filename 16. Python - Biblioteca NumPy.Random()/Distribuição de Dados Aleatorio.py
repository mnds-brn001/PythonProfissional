from numpy import random

arr=[3,5,7,9]
prob= [0.1, 0.3, 0.6, 0.0] # Valores devem somar até o máximo de 1
# p: Probability
# x= random.choice(arr, p=prob, size=(100))
x= random.choice(arr, p=prob, size=(3,5))

print(x)