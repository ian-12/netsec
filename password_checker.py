import random
import string


def main():
    result = generate_random_string()
    print(f"Generated password: {result}")


def generate_random_string():
    """Generate a random string of letters, digits and special characters."""
    random_string = ""
    string_length = random.randint(8, 20)
    while len(random_string) <= string_length:
        random_string += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return random_string


main()
