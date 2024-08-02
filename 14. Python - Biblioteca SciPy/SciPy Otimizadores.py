# Encontre a raiz da Equação: x+cos(x):

from scipy.optimize import root, minimize
from math import cos

def eqn(x):
    return x + cos(x)

myroot=root(eqn, 0)


print(myroot.x)
print(myroot)
print("##################################################")

# Minimizar a função x^2 + x + 2 com o algoritmo BFGS:
def eqn2(x):
    return x**2 + x + 2

mymin= minimize(eqn2, 0, method='BFGS')
print(mymin)