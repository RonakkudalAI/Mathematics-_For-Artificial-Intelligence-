import numpy as np

v = np.array([3, -4, 2])

print("L2:", np.linalg.norm(v))          # default
print("L1:", np.linalg.norm(v, ord=1))
print("L∞:", np.linalg.norm(v, ord=np.inf))
print("L0:", np.count_nonzero(v))        # special case