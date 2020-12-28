'''
I'm using one of my three late days.
Assignment 4: Password.py
This program ask the user to enter a password and checks if it matches this criteria for a strong password:
a. The password must be 8 or more characters long
b. It should contain at least 1 uppercase letter
c. It should contain at least 3 numbers
d. It should at least once contain the word ‘cat’
e. It should contain 1 question mark (?)
f. There can not be any spaces in the password
The program tells the user if it's missing any of these, and tells the user what is missing.
Sophia Crawford
'''
password = input("Enter a password:")

if len(password) < 8:
    password = input("Password must be 8 or more characters long. Enter another password:")
if password.count(' ') >= 1:
    password = input("Password cannot contain spaces. Enter another password:")
if password.count('?') != 1:
    password = input("Password must contain one '?'. Enter another password:")
if password.find('cat') == -1:
    password = input("Password must contain the (substring) 'cat', in lowercase. Enter another password:")
if password.count('0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9') < 3:
    password = input("Password must contain at least three numbers. Enter another password:")
if 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z' not in password:
    password = input("Password must contain at least one uppercase letter. Enter another password:")
print('Success!')

# it started fine...
