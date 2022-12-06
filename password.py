# A simple program to check if the password entered is valid or not

password = input("Enter the password: ")
count = [0]*6                                                                 # creating a count list with 5 elements 
for ch in password:
    count[0] += 1                                                             # counting the length of the password
    if ord(ch)>=65 and ord(ch)<=90:                                           # checking for uppercase alphabets
        if count[1] == 0:
            count[1] = 1
    elif ord(ch)>=97 and ord(ch)<=122:                                        # checking for lowercase alphabets 
        if count[2] == 0:
            count[2] = 1
    elif ord(ch)>=33 and ord(ch)<=47 or ord(ch)>=58 and ord(ch)<=64:          # checking for symbol
        if count[3] == 0:
            count[3] = 1
    elif ord(ch)>=48 and ord(ch)<=57:                                         # checking for digits
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
