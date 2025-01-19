import string
import secrets
import numpy

def length_numb():
    while True:
        try:
            length = int(input("Input length of the password\n"))
            break
        except:
            print("MISTAKE! Please enter number")
            continue
    return length


def bool_sp_characters():
    while True:
        try:
            numbers = input("\nDo you want special characters in your password? Write Yes or No\n")
            if numbers == "yes" or numbers == "Yes":
                return True
            elif numbers == "No" or numbers == "no":
                return False
            else:
                print("MISTAKE! Enter Yes or No")
        except:
            print("MISTAKE! Enter Yes or No")
            continue

def bool_numbers():
    while True:
        try:
            numbers = input("\nDo you want numbers in your password? Write Yes or No\n")
            if numbers == "yes" or numbers == "Yes":
                return True
            elif numbers == "No" or numbers == "no":
                return False
            else:
                print("MISTAKE! Enter Yes or No")
        except:
            print("MISTAKE! Enter Yes or No")
            continue

def bool_cap_letters():
    while True:
        try:
            numbers = input("\nDo you want capital Letters in your password? Write Yes or No\n")
            if numbers == "yes" or numbers == "Yes":
                return True
            elif numbers == "No" or numbers == "no":
                return False
            else:
                print("MISTAKE! Enter Yes or No")
        except:
            print("MISTAKE! Enter Yes or No")
            continue

def generate_pass(length,all_array):
    password = ""
    for i in range(length):
        password += secrets.choice(all_array)
    return password


def main():
    print("Hello, It's password generator!\n")
    length = length_numb()
    incl_numbers = bool_numbers()
    incl_capital = bool_cap_letters()
    incl_characters = bool_sp_characters()
    low_letters=list(string.ascii_lowercase)
    cap_letters=list(string.ascii_uppercase)
    numbers = [str(i) for i in range(10)]
    sp_characters = list("!@#$%^&*()_+-=[]{}|;:',.<>?/`~")
    all_array = low_letters + cap_letters + numbers + sp_characters
    if not incl_numbers:
        all_array = numpy.setdiff1d(all_array, numbers)
    if not incl_capital:
        all_array = numpy.setdiff1d(all_array, cap_letters)
    if not incl_characters:
        all_array = numpy.setdiff1d(all_array, sp_characters)
    print("\nHere's your password!")
    password = generate_pass(length,all_array)
    print(password)


if __name__ == '__main__':
    main()
