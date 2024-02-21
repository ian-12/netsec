import random
import string
import re


def main():
    result = generate_random_string()
    print(f"Generated password: {result}")
    get_valid_input()


def generate_random_string():
    """Generate a random string of letters, digits and special characters."""
    random_string = ""
    string_length = random.randint(8, 20)
    while len(random_string) <= string_length:
        random_string += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return random_string


def get_valid_input():
    """Get user input"""
    user_input = input("Type your password: ")
    if is_password_valid(user_input):
        print(f"Your password meets the requirements, length {len(user_input)}")
        return user_input
    else:
        print("Your password does not meet the requirements. Try again.")
        return get_valid_input()


def is_password_valid(user_input):
    """Check if the user input meets the requirements."""
    is_ok1 = bool(re.search("[a-z]", user_input))
    is_ok2 = bool(re.search("[A-Z]", user_input))
    is_ok3 = bool(re.search("[0-9]", user_input))
    is_ok4 = bool(re.search("[+\-!\"#$%&'()*,./:;<=>?@\[\]^_`{|}~]", user_input))
    return is_ok1 and is_ok2 and is_ok3 and is_ok4


main()
