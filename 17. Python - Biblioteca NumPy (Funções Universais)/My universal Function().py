import numpy as np

def myadd(x,y):
    return x+y

myadd= np.frompyfunc(myadd, 2, 1)
addmatriz= np.frompyfunc(myadd, 2, 1)

x= [1, 2, 3, 4]
y= [5, 6, 7,8]
z= addmatriz(x,y) # z= myadd(x,y) 

print(z)

print(type(np.add)) # type:Função Universal
print(type(np.concatenate)) # Type ArrayFunctionDispatcher

if type(myadd) == np.ufunc:
    print("Sim é uma Função Univesal")
else:
    print("Não é uma Universal Function.")
