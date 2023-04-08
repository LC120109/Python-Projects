import numpy as np

a = np.array([[1,2,3],
              [4, "Hello",6],
              [7,8,9]])

print(a.dtype) #<U11 --> string with less than 11 characters
print(type(a[0][0])) #is considered a string bc there's a string in the array
print(a[0][0].dtype) #<U1 --> less than 1 character
 
a = np.array([[1,2,3],
              [4, "5",6],
              [7,8,9]], dtype=np.int32)

print(a.dtype) # if a number is a string, then you can convert it, else it's not possible
