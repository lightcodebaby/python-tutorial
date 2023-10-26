import numpy as np
import numpy.linalg as la

# Slicing

a = np.round(10 * np.random.rand(2, 3))
print(a + 3)

print(a)
print(np.arange(2).reshape(2, 1))
print(a + np.arange(2).reshape(2, 1))

a = np.round(10 * np.random.rand(2, 3))
b = np.round(10 * np.random.rand(2, 2))

c = np.hstack((a, b)) # hstack for horizontal stack and vstack for vertical stack
print(c)

a = np.random.permutation(np.arange(10))
print(a.sort())
print(a.sort()[::-1])

a = np.array(["fgh", "cde", "abc"])
print(a.sort())

