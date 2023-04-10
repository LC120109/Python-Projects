import numpy as np

#a = np.array([[1,2,3,4,5],
#              [6,7,8,9,10],
#              [11,12,13,14,15],
#              [16,17,18,19,20]])

#np.save("myarray.npy", a)

#a = np.load("./Numpy_Learning/myarray.npy")
#print(a)

#np.savetxt("myarray.csv", a, delimiter=",")

a = np.loadtxt("./Numpy_Learning/myarray.csv", delimiter=",")
print(a)