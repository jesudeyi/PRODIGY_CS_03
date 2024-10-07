import string
import os

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # macOS/Linux





def get_password():
    print("Welcome to Password Complexity Checker")
    password = input("Enter your password: ")
    return password

def check_len(password):
    length = len(password)
    return length

def check_upper(password):
    hasUpper = False
    for char in password:
        if char.isupper():
            hasUpper = True
            break
    return hasUpper

def check_lower(password):
    hasLower = False
    for char in password:
        if char.islower():
            hasLower = True
            break
    return hasLower

def check_digit(password):
    hasDigit = False
    for char in password:
        if char.isdigit():
            hasDigit = True
            break
    return hasDigit

def check_special_character(password):
    hasSpChar = False
    for char in password:
        if char in string.punctuation:
            hasSpChar = True
            break
    return hasSpChar

choice = 'y'
while choice == 'y' or choice == 'Y':
    password = get_password()
    if password:
        if check_len(password) < 10:
            print("Password should be at least 10 characters long!")
        else:
            print ("Your password is long enough.")
        
        if not check_upper(password):
            print("Your password should contain an upper case character!")

        if not check_lower(password):
            print("Your password should contain a lower case character!")

        if not check_digit(password):
            print("Your password should contain a digit!")
        else:
            print ("Your password has enough digits.")

        if not check_special_character(password):
            print("Your password should contain a special character!")
        else:
            print ("Your password has enough special characters.")

    else:
        print("Password cannot be empty.")

    choice = input("Do you want to check another password? \ny/n: ")
    clear_screen()