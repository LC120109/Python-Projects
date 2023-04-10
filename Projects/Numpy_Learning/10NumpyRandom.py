import numpy as np

#possible to randomize whole arrays
numbers = np.random.randint(90, 100, size=(2,3,4)) #ranges also possible

print(numbers)

print("\n")
numbers = np.random.binomial(10, p=0.5, size=(5,10)) #example use: heads or tails
print(numbers)

print("\n")
numbers = np.random.choice([10,20,30,40,50], size=(5,10))
print(numbers)