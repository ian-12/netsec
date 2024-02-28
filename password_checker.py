import random
import string
import re
import hashlib

"""Task 1"""


def main():
    """Main Menu"""
    print_menu()
    get_menu_choice()


def get_menu_choice():
    user_input = int(input("Enter choice: "))
    while user_input < 1 or user_input > 6:
        user_input = int(input("Enter choice: "))
    if user_input == 1:
        generate_password()
    elif user_input == 2:
        get_valid_input()
    elif user_input == 3:
        save_to_file()
    elif user_input == 4:
        salt_hash_password()
    # elif user_input == 5:
    #     verify_password()
    else:
        exit()


def print_menu():
    print("1. Generate Password")
    print("2. Type new Password")
    print("3. Write string into file")
    print("4. Hash Function")
    print("5. Verify Password")
    print("6. Exit")
    print("------------------------")


def generate_password():
    """Task 1- Generate Password"""
    string_password = ''
    string_length = random.randint(8, 20)
    while len(string_password) <= string_length:
        string_password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    print(f"Generated password: {string_password}")
    choice = input("Use this password? (Y/N): ").upper()
    if choice == "Y":
        return string_password
    else:
        get_valid_input()


def get_valid_input():
    """Task 2 - Input Validation"""
    new_password = input("Type new Password: ")
    input_length = len(new_password)
    is_ok1, is_ok2, is_ok3, is_ok4 = is_valid(new_password)
    while input_length < 8 or not is_ok1 or not is_ok2 or not is_ok3 or not is_ok4:
        print("Password does not meet the requirements")
        print("Password must be at least 8 characters long and contain at least one of each of the following:")
        print("Lowercase letter, Uppercase letter, Number, Special character")
        print("------------------------")
        task2_input = input("Task 2 - Input: ")
        input_length = len(task2_input)
        is_ok1, is_ok2, is_ok3, is_ok4 = is_valid(new_password)
    print(f"Your password is {new_password}, and the length is {input_length} characters long")


def is_valid(new_password):
    is_ok1 = bool(re.search("[a-z]", new_password))
    is_ok2 = bool(re.search("[A-Z]", new_password))
    is_ok3 = bool(re.search("[0-9]", new_password))
    is_ok4 = bool(re.search("[+\-!\"#$%&'()*,./:;<=>?@\[\]^_`{|}~]", new_password))
    return is_ok1, is_ok2, is_ok3, is_ok4


"""Task 3 - Write string into file"""

# def save_to_file():
#     file = open('passwords.txt', 'w')
#     file.flush()
#     file.write(string_password)  # String to write in file
#     file.close()
#     print("Task 3 - Your password has been written to passwords.txt")
#     print("------------------------")
#
#
# save_to_file()

"""Task 4 - Hash Function"""


def salt_hash_password():
    salt = random.uniform(0.0, 5.0)  # Generate a random salt
    salted_password = string_password + str(salt)
    salted_hash_password = hashlib.sha256(salted_password.encode()).hexdigest()
    print(f"Salted hash password: {salted_hash_password}")
    # Use the salted has password to verify a new password attempt
    new_password = input("Enter new password: ")
    new_salted_password = new_password + str(salt)
    new_salted_hash_password = hashlib.sha256(new_salted_password.encode()).hexdigest()
    print(new_salted_hash_password)


# hashed_password = hashlib.sha512()
# hashed_password.update(salt)
# hashed_password.update(string_password.encode())
# hashed_password.digest()
# print(f"Hashed password: {hashed_password.hexdigest()}")


# """Task 3"""
# file = open('passwords.txt', 'w')
# file.flush()
# file.write(hashed_password.hexdigest())  # String to write in file
# file.close()
#
# file = open('passwords.txt')
# user_password_input = input("Enter Password: ")
# password_to_compare = file.readline()
# print(password_to_compare)

"""Task 5"""
# Read a string (pasword) from the keyboard input (ELLIOT) YUHANG Feng
# final_password = input("")

# Call your hash function to verify the password

# Close main function
main()
