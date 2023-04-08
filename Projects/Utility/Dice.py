import random
import sys

while True:
    personal = input("Roll the dice? Y/N: ")
    if personal == "N": 
        sys.exit()
    elif personal == "Y":
        print(random.randint(1, 6))