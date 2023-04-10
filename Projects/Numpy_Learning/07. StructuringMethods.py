import numpy as np

a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])

"""
print(a.shape)

#print(a.reshape((5,4))) #it has to work with your array
#print(a.reshape((20,))) #inline
print(a.reshape((2, 2, 5))) #2 collections, 2 lists, with 5 elements

a.resize((10, 2)) #this applies it immediately without having to assign it
print(a)

print(a.flatten()) # 1D & prints a flattened copy
print(a.ravel()) # only prints a flatten view

#Demonstration: difference between flatten vs ravel

var1 = a.flatten()
var1[2] = 100
print(var1)
print(a) #doesn't change

var1 = a.ravel()
var1[2] = 100
print(var1)
print(a) #changes it


var = [v for v in a.flat]
print(var)
"""

print(a.transpose()) #swaps columns and rows
print(a.T)
print(a.swapaxes(0, 1)) #swaps 2 axes