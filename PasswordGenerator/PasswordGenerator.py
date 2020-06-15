import random
import string

'''
A programme which generates a random password for the user. Ask the user how long they want their password to be,
and how many letters and numbers they want in their password. Have a mix of upper and lowercase letters, as well as numbers and symbols. 
The password should be a minimum of 6 characters long.
'''
MINIMUM_PW_LENGTH = 6


# get password length
# minimum of 6 characters long
def get_password_length():
    valid = False
    while not valid:
        try:
            pw_length = int(input("How long do you want your password to be?\n"))
            if pw_length >= MINIMUM_PW_LENGTH:
                return pw_length
            else:
                print("Password must be a minimum of 6 characters long")
        except Exception:
            print("Invalid input try again.")


# get the number of letters
# Mix of lower and uppercase characters
def get_letters():
    valid = False
    while not valid:
        try:
            num_letters = int(input("How many letters do you want your password to have?\n"))
            return num_letters
        except Exception:
            print("Invalid input try again.")


# get the number of numbers
    # mix of numbers and symbols
def get_numbers():
    valid = False
    while not valid:
        try:
            num_letters = int(input("How many numbers do you want your password to have?\n"))
            return num_letters
        except Exception:
            print("Invalid input try again.")

#format of number portion of pw
def numbers_format(numbers):
    valid = False
    while not valid:
        try:
            numbs = int(input("Enter the number of numbers case letters you want to have:\n"))
            symbols = int(input("Enter the number of symbols letters you want to have:\n"))
            if numbs + symbols == numbers:
                return numbs, symbols
            else:
                print("The inputs exceeded the limit of the number of numbers you wanted.\nTry different inputs.")
        except Exception:
            print("Invalid inputs try again")


#generate numbers
def generate_numbers(numbs, symbols):
    my_pw = ''
    for i in range(numbs):
        my_pw += random.choice(string.digits)
    for i in range(symbols):
        my_pw += random.choice(string.punctuation)
    return my_pw


# check valid input
def validation(pw_length, letters, numbers):
    return True if pw_length == (numbers + letters) else False


#get number of upper and lowercase letters
def letters_format(letters):
    valid = False
    while not valid:
        try:
            lower_case = int(input("Enter the number of lower case letters you want to have:\n"))
            upper_case = int(input("Enter the number of upper case letters you want to have:\n"))
            if lower_case + upper_case == letters:
                return lower_case, upper_case
            else:
                print("The inputs exceeded the limit of the number of letters you wanted.\nTry different inputs.")
        except Exception:
            print("Invalid inputs try again")


#generate the letters for password
def generate_letters(lower_case_number, upper_case_number):
    my_pw = ''
    for i in range(lower_case_number):
        my_pw += random.choice(string.ascii_lowercase)
    for i in range(upper_case_number):
        my_pw += random.choice(string.ascii_uppercase)
    return my_pw


# generate the pw
def generate():
    valid = False
    my_pw =''
    while not valid:
        pw_length = get_password_length()
        letters = get_letters()
        lower_case_number, upper_case_number = letters_format(letters)
        numbers = get_numbers()
        numbs,symbols = numbers_format(numbers)
        if validation(pw_length, letters, numbers):
            #generate here
            my_pw = generate_letters(lower_case_number, upper_case_number)
            my_pw += generate_numbers(numbs, symbols)
            print(f'Your Password is: {my_pw}')
            valid = True
        else:
            print("Cannot use the inputs please try different inputs.")


def main():
    generate()


if __name__ == "__main__":
    main()
