import numpy as np
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2,7,6,8])
print(x)