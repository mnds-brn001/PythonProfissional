import numpy as np

arr= np.array([41, 42,43,44])

x=[True,False,True,False]

filter_arr= [] # Inicializando a lista
for elemento in arr:
    if elemento > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

# filter_arr= [] # Inicializando a lista
# for elemento in arr:
#     if elemento %2 == 42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)



newarr= arr[filter_arr]
print(filter_arr)
print(newarr)

# newarr= arr[x]
# print(newarr)