import string  # This module has methods which has values all alphabets, digits, characters
import random  # This is imported to shuffle the values randomly to get a stronger password


def generate_password():  # Method called to create a password
    try:
        length = int(input("Enter the length of the password required: "))
        s = []  # Empty list declared
        s.extend(alphabets)  # We use extend() method to concatenate the values from
        s.extend(digits)     # string module to list s[]
        s.extend(characters)
        random.shuffle(s)    # shuffles the values in the list randomly for strong password
        print("The Generated password is:", "".join(s[:length]))  # join is used to join all the list elements into
    except ValueError:                                            # a single string
        print("Please enter numbers only...!!")  # Handles exception when value other than int is given
        generate_password()


if __name__ == '__main__':            # Will make sure the file is running with in code file
    alphabets = string.ascii_letters  # Taking values string from module
    digits = string.digits
    characters = string.punctuation
    print('"Password generator by Teja_Sandeep_Reddy"')
    generate_password()

# Password generator By Teja_Sandeep_Reddy
