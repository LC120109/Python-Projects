import numpy as np
"""
a1 = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])

a2= np.array([[11,12,13,14,15],
              [16,17,18,19,20]])

a = np.concatenate((a1, a2), axis=0) #0=rows
print(a)
a = np.concatenate((a1, a2), axis=1) #1=columns
print(a)

a = np.stack((a1, a2))
print(a)
a = np.vstack((a1, a2))
print(a)
a = np.hstack((a1, a2))
print(a)
"""
a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])

print(np.split(a, 4, axis=0)) # middle number= how many arrays

