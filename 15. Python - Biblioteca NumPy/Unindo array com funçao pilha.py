import numpy as np

arr1= np.array([1,2,3])
arr2= np.array([4,5,6])

# arr = np.stack((arr1, arr2), axis=1) # Pilha
# arr= np.hstack((arr1 arr2)) # Horizontal Stack
# arr= np.vstack((arr1, arr2)) # Vertical Stack
arr= np.dstack((arr1, arr2)) # Dimensional Stack

print(arr)