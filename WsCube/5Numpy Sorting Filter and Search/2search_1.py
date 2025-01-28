import numpy as np

ar = np.array([3,4,1,7,8])
s = np.where(ar == 4)
print(s)

x = np.where(ar % 2 == 0)
print(x)