import numpy as np
from math import log

nplog= np.frompyfunc(log, 2, 1)

arr = np.arange(1, 10)

print(arr)
print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))
print(nplog(100,15)) # 100 na base 15
