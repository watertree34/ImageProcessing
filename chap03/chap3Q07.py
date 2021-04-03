import numpy as np

a=np.random.rand(2,3)
print(a)
print(a.flatten())
print(np.ravel(a))
print(np.reshape(a,(-1,)))
print(a.reshape(-1,))