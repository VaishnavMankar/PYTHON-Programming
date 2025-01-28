import numpy as np

ar = np.array([20,30,40,50])

fa = [True,False,True,False]

new = ar[fa]
print(new)

fb = ar > 35
new = ar[fb]
print(new)