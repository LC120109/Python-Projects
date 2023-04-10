import numpy as np

"""
a = np.full((2,3,4), 9) #shape and number
print(a)

a = np.zeros((10,5,2))
print(a)

a = np.ones((10,5,2))
print(a)

a = np.empty((5,5,5)) #allocates space without initializing the values
print(a)


x_values = np.arange(0, 1000, 5) #start, stop, step size
print(x_values)
"""

x_values = np.linspace(0, 1000, 1001) #start, stop, how many values
print(x_values)