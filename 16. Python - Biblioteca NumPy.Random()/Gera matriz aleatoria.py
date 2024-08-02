from numpy import random

# x= random.randint(100, size=(5)) # Matriz 1-D com 5 Elementos
# x= random.randint(100, size=(3,5)) # Matriz 2-D com 5 Elementos

# x= random.rand(5)
# x= random.rand(3,5)

#x= random.choice([3,5,7,9]) # Escolhe aleatóriamente o valor no conjunto

x= random.choice([3,5,7,9], size=(3,5))

print(x)