import numpy as np

arr = np.array([1,2,3,4,5])
x= arr.copy()
y= arr.view()
# arr[0]= 42
# x[3] = 31
# print(arr)
# print(x)

print(x.base)
print(y.base)