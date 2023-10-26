import numpy as np

a = np.arange(start=0, stop=100, step=2)
print(a)

b = np.zeros(shape=100)
print(b)

c = np.random.permutation(np.arange(10))
print(c)

d = np.random.randint(low=10, high=20)
print(d)

e = np.random.rand(1000)
f = np.random.randn(1000)
print(e)
print(f)

g = np.arange(100).reshape(4, 5, 5)
print(g)

h = np.empty(5, 5)
i = np.empty_like(g)

print(h)
print(i)
