# A simple program to check if the password entered is valid or not
# This program makes use of string methods

password = input("Enter the password: ")
count = [0]*6                                                                 # creating a count list with 5 elements 
for ch in password:
    count[0] += 1                                                             # counting the length of the password
    if ch.isupper():                                                          # checking for uppercase alphabets
        if count[1] == 0:
            count[1] = 1
    elif ch.islower():                                                        # checking for lowercase alphabets 
        if count[2] == 0:
            count[2] = 1
    elif not ch.isalnum():                                                    # checking for symbol
        if count[3] == 0:
            count[3] = 1
    elif ch.isdigit():                                                        # checking for digits
        if count[4] == 0:
            count[4] = 1
    count[5] = count[1] + count[2] + count[3] +count[4]                       # totaling the count
                                                                                  
if count[0] >= 8:                                                             # Checking if the password entered satisfies the requirement
    if count[5] == 4:
        print("Password successfully set.")
    elif count[5] != 4:
        print("Password set unsuccessful.")
        if count[1] == 0:
            print("No uppercase letter in password.")
        if count[2] == 0:
            print("No lowercase letter in password.")
        if count[3] == 0:
            print("No symbol in the password.")
        if count[4] == 0:
            print("No digit in the password.")
else:
    print("Password set unsuccessful.")
    print("Password less than 8 characters.")
    if count[1] == 0:
        print("No uppercase letter in password.")
    if count[2] == 0:
        print("No lowercase letter in password.")
    if count[3] == 0:
        print("No symbol in the password.")
    if count[4] == 0:
        print("No digit in the password.")
