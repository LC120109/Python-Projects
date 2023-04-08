#Tutorial by NeuralNine on Youtube

import numpy as np

#ordinary python lists
"""
a = [1, 2, 3, 4, 5]
print(a)
print(a[1])
print(a[1:4])
print(a[-1])
"""
"""
a = np.array([1,2,3,4,5])
print(a) #numpy arrays are seperated by spaces, not commas
print(type(a))
print(a[1])
print(a[1:4])

a[2] = 10
print(a)
"""

a_mul = np.array([[1,2,3], [4,5,6], [7,8,9]])
"""
print(a_mul[0])
print(a_mul[0, 1])
"""
print(a_mul.shape)
print(a_mul.ndim)
print(a_mul.size)
print(a_mul.dtype)