import random
import string
import re
import hashlib

"""Task 1"""


def main():
    """Main Menu"""
    display_menu()
    choice = get_choice()
    while choice != 6:
        if choice == 1:
            result = generate_password()
        elif choice == 2:
            result = get_valid_input()
        elif choice == 3:
            outfile = save_to_file(result)
        elif choice == 4:
            hash_password = salt_hash_password(result)
        elif choice == 5:
            verify_hash(hash_password)
        else:
            print("Invalid choice")
        display_menu()
        choice = get_choice()
    print("Goodbye")


def display_menu():
    print("1. Generate Password")
    print("2. Type own password and validate it")
    print("3. Save password to file")
    print("4. Add salt and hash")
    print("5. Verify password with hash")
    print("6. Quit")


def get_choice():
    return int(input("Enter choice: "))


def generate_password():
    """Task 1- Generate Password"""
    string_password = ''
    string_length = random.randint(8, 20)
    for i in range(string_length):
        string_password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    print(f"Generated password: {string_password}")
    return string_password


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
        new_password = input("Type new Password: ")
        input_length = len(new_password)
        is_ok1, is_ok2, is_ok3, is_ok4 = is_valid(new_password)
    print(f"Your password is {new_password}, and the length is {input_length} characters long")
    return new_password


def is_valid(new_password):
    is_ok1 = bool(re.search("[a-z]", new_password))
    is_ok2 = bool(re.search("[A-Z]", new_password))
    is_ok3 = bool(re.search("[0-9]", new_password))
    is_ok4 = bool(re.search("[+\-!\"#$%&'()*,./:;<=>?@\[\]^_`{|}~]", new_password))
    return is_ok1, is_ok2, is_ok3, is_ok4


def save_to_file(password):
    """Task 3 - Write string into file"""
    file = open('passwords.txt', 'w')
    file.flush()
    file.write(password)  # String to write in file
    file.close()
    print("Your password has been written to passwords.txt")
    return file


"""Task 4 - Hash Function"""


def salt_hash_password(string_password):
    salt = random.uniform(0.0, 5.0)  # Generate a random salt
    salted_password = string_password + str(salt)
    salted_hash_password = hashlib.sha256(salted_password.encode()).hexdigest()
    print(f"Salted hash password: {salted_hash_password}")
    return salted_hash_password, salt

def verify_hash(hash_password):
    """Verify the password"""
    user_input = input("Enter your password: ")
    pass_to_verify = user_input + str(hash_password[1])
    salted_hash_password = hashlib.sha256(pass_to_verify.encode()).hexdigest()
    if hash_password[0] == salted_hash_password:
        print("Password verified")
    else:
        print("Password not verified")


# Call your hash function to verify the password

main()
