import numpy as np

"""
a = np.array([1,2,3])

a = np.append(a, [7,8,9]) #else it doesn't add the 7,8,9

print(a)

a = np.insert(a, 3, [4,5,6]) #in position 3

print(a)
"""
a = np.array([[1,2,3],
              [4,5,6]])

print(np.delete(a, 1, 0)) #if we only type 1 then it will delete the 2, like this whole 2. row

print(np.delete(a, 1, 1)) #deletes everything in the 2. column