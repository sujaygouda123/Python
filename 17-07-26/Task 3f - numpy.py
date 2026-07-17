"""
Python Library — numpy (numerical arrays)
Requires: pip install numpy
Run this file directly: py "Task 3f - numpy.py"
"""

import numpy as np

# ------------------------------------------------------------------
# 1. Creating an array
# ------------------------------------------------------------------
print("create array")
arr = np.array([1, 2, 3, 4, 5])
print(arr)                                 # [1 2 3 4 5]
print(arr.shape)                           # (5,)
print()

# ------------------------------------------------------------------
# 2. Element-wise arithmetic  -> no loop needed
# ------------------------------------------------------------------
print("element-wise arithmetic")
print(arr * 2)                             # [ 2  4  6  8 10]
print(arr + 10)                            # [11 12 13 14 15]
print()

# ------------------------------------------------------------------
# 3. 2D arrays / matrices
# ------------------------------------------------------------------
print("2D array")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)                              # [[1 2 3] [4 5 6]]
print(matrix.shape)                        # (2, 3)
print(matrix.T)                            # transposed: [[1 4] [2 5] [3 6]]
print()

# ------------------------------------------------------------------
# 4. Aggregate functions
# ------------------------------------------------------------------
print("aggregates")
print(arr.sum())                           # 15
print(arr.mean())                          # 3.0
print(arr.max())                           # 5
print()

# ------------------------------------------------------------------
# 5. Useful array builders
# ------------------------------------------------------------------
print("builders")
print(np.arange(0, 10, 2))                 # [0 2 4 6 8]
print(np.zeros(3))                         # [0. 0. 0.]
print(np.linspace(0, 1, 5))                # [0.   0.25 0.5  0.75 1.  ]
