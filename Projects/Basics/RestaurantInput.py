name = ""
while not name:
    name = input("Enter your name: ")

print(f"Okay, {str(name).title()}.")
numOfGuests = input("How many guests will you have? ")

if numOfGuests:
    print(f"Okay, {int(numOfGuests)} people.")

print("Done")
