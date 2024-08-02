import numpy as np

arr = np.array([6,7,8,9]) # 0 1 2 3 

#x= np.searchsorted(arr,7)
#x= np.searchsorted(arr,7, side="right")
x= np.searchsorted(arr,[2,4,6])


print(x)