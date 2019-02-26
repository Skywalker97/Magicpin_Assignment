import re
#The code below is subject to the following assumptions
#I have assumed that if a comma is followed by a space, it is part of the password
#Assuming that commas cannot be a part of a password

def validate(password):
    flag = 0
    while True:
        if len(password) < 6:
            flag = -1
            print(password + " Failure Password must be at least 6 characters long.")
            break
        elif len(password) > 12:
            flag = -1
            print(password + " Failure Password must be at max 12 characters long.")
            break
        elif not re.search("[a-z]", password):
            flag = -1
            print(password + " Failure Password must contain at least one letter a-z.")
            break
        elif not re.search("[0-9]", password):
            flag = -1
            print(password + " Failure Password must contain at least one digit from 0-9.")
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            print(password + " Failure Password must contain at least one letter from A-Z.")
            break
        elif not re.search("[*$_#=@]", password):
            flag = -1
            print(password + " Failure Password must contain at least one character from *$_#=@.")
            break
        elif re.search("[%!()]", password):
            flag = -1
            print(password + " Failure Password cannot contain %!)(.")
            break
        else:
            flag = 0
            print(password + " Success")
            break



#Accepting list of comma separated passwords
passwords = input("Enter a comma separated list of passwords")
#Removing commas and splitting the string into individual passwords
#The list stores the passwords
list = passwords.split(",")

for i in list:
    validate(i)
