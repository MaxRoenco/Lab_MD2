import re


def has_lowercase(string):
    for i in range(len(string)):
        if 122 >= ord(string[i]) >= 97:
            return True
    else:
        return False


def has_uppercase(string):
    for i in range(len(string)):
        if 90 >= ord(string[i]) >= 65:
            return True
    else:
        return False


def has_numeric(string):
    for i in range(len(string)):
        if 57 >= ord(string[i]) >= 48:
            return True
    else:
        return False


def has_special(string):
    for i in range(len(string)):
        if 47 >= ord(string[i]) >= 33 or 64 >= ord(string[i]) >= 58 or 96 >= ord(string[i]) >= 91:

            return True
    else:
        return False


while True:
    check_letters = False
    check_lowercase = False
    check_uppercase = False
    check_numeric = False
    check_special = False
    check_repeatedchars = False
    check_consecutiveNumbers = False
    password = input("Input your password: ")

    if len(password) < 8:
        print(f"You need to add {8 - len(password)} letters!")
    elif len(password) > 20:
        print(f"Your password is too long, you need to remove {len(password) - 20} letters")
    else:
        check_letters = True
    if not has_lowercase(password):
        print("It should has a minimum of 1 lower case letter [a-z].")
        break
    else:
        check_lowercase = True
    if not has_uppercase(password):
        print("It should has a minimum of 1 upper case letter.")
        break
    else:
        check_uppercase = True
    if not has_numeric(password):
        print("It should has minimum of 1 numeric character [0-9].")
        break
    else:
        check_numeric = True
    if not has_special(password):
        print("It should have a minimum of 1 special character: ~`!@#$%^&*()-_+={}[]|\;:\"<>,./?")
        break
    else:
        check_special = True
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            print(f"Incorrect password, it contains three repeating characters in a row.")
            break
    else:
        check_repeatedchars = True
    for i in range(len(password) - 1):
        if password[i].isdigit() and password[i + 1].isdigit():
            if int(password[i]) + 1 == int(password[i + 1]) or int(password[i]) == int(password[i + 1]) + 1:
                print(f"Incorrect password, it contains consecutive numbers.")
                break
    else:
        check_consecutiveNumbers = True
    if check_special and check_repeatedchars and check_numeric and check_uppercase and check_lowercase and check_letters and check_consecutiveNumbers:
        print("Good password")
        break

