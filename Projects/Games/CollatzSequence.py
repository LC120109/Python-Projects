import sys
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
     
    else:
        result = 3 * number + 1
        print(result)
        return result
    

while True:
    message = input("Enter a number: \n")
    try:
        while message != 1:
            message = collatz(int(message))

    except ValueError:
        print("Enter a positive number")

