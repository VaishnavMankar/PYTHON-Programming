import numpy as np

ar = np.array([1,2,3,4,5,6,7,8])
ss = np.searchsorted(ar,2)  #for using searchsort the array should be sorted
print(ss)