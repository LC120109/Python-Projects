"""
The goal of this project is to have a contact book, where we can add, edit, delete or view our contacts in the command line (and maybe in a GUI in the future).
Not finished.
"""

import sys
contacts = {}

print("Entering Contact Book!")

while True:
    while True:
        initial = input("What do you want to do? add/edit/delete/view/quit: ")
        if initial == "quit":
            sys.exit()
        if initial == "add" or initial == "edit" or initial == "delete" or initial == "view":
            break

    if initial == "add":
        contacts["first_name"] = input("Tell me their first name: ")
        contacts["phone_number"] = input("Tell me their phonw number: ")
        print(contacts)
