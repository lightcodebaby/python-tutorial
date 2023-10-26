import numpy as np
import numpy.linalg as la

# Slicing

a = np.arange(start=0, stop=100)
b = a[3:10]
b[0] = 1200
print(a)
print(b)

a = np.arange(start=0, stop=100)
b = a[3:10].copy()
b[0] = 1200
print(a)
print(b)

print(a[::5])
print(a[::-5])
print(a[::-1])

a = np.arange(start=0, stop=100)
b = a[3:10]
b[0] = 1200
index = np.argwhere(a == 1200)[0][0]
a[index] = 3

a = np.round(10 * np.random.rand(5, 4))
a.sort(axis=0)
print(a)

print(a[1, 2])
print(a[1, :])
print(a[:, 1])
print(a[1:3, 2:4])
print(a.T)

print(la.inv(np.random.rand(3, 3)))

# Masking

a = np.arange(start=0, stop=100)
b = a[1, 3, 5]

print(b)
print(
    a[(a > 30) & (a < 40)]
)  # & for arrays, and for single items (same for | or) (same for ~ not)
