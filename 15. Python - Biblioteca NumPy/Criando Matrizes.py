import numpy as np

# Matrizes 0-D
a = np.array(42)
print(a)

# Matrizes 1-D
b = np.array([1,2,3,4,5])

# Matrizes 2-D
c = np.array([[1,2,3], [4,5,6]])

# Matrizes 3-D
d = np.array(
    [
        [
                [1,2,3],[4,5,6]
            ],
            [
                [7,8,9],[0,2,4]
            ]
            ]
)
valores= [1,2,3,4,5]
e= np.array(valores, ndmin=5)

print(e)
print(type(e))

print(a.ndim) # .ndim: number of dimensions
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)
