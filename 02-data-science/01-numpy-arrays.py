import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype="i")
b = np.array((6, 7, 8, 9, 10), dtype="f")

print(a)
print(b)
print(type(a))
print(type(b))
print(a.dtype)
print(b.dtype)

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim)
print(a[0, 2])

b = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(b.ndim)
print(b.shape)
print(b.shape[1])
print(b.size)
