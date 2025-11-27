import numpy as np
arr = np.array([9, 7, 8,10, 5,3])
x = np.searchsorted(arr, 3)
print(x)