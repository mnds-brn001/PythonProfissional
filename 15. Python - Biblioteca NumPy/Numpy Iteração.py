import numpy as np

# arr = np.array([1,2,3])
#arr = np.array([[1,2,3],[4,5,6]])

arr=np.array([
              [[1,2,3], [4,5,6]],
              [[7,8,9], [10,11,12]]
              ])

# Para dimensão na matriz temos que adicionar um loop for
for x in arr: # 1-D
    for y in x: # 2-D
        for z in y: # 3-D
            print(z)