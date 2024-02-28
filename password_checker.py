import random
import string
import re
import hashlib

"""Task 1"""
string_password = ''
string_length = random.randint(8, 20)
while len(string_password) <= string_length:
    string_password += random.choice(string.ascii_letters + string.digits + string.punctuation)
print(f"Task 1 - Generated password: {string_password}")
print("------------------------")

# """Hash test"""
# m = hashlib.sha256()
# m.update(string_password.encode())
# print(m.digest())
# print(m.hexdigest())


"""Task 2"""
task2_input = input("Task 2 - Input: ")
input_length = len(task2_input)
is_ok1 = bool(re.search("[a-z]", task2_input))
is_ok2 = bool(re.search("[A-Z]", task2_input))
is_ok3 = bool(re.search("[0-9]", task2_input))
is_ok4 = bool(re.search("[+\-!\"#$%&'()*,./:;<=>?@\[\]^_`{|}~]", task2_input))
if is_ok1 and is_ok2 and is_ok3 and is_ok4:
    print(f"Input OK, length is {input_length}")
else:
    print("Input NOT OK")
print("------------------------")

"""Task 4 - Hash Function"""

salt = random.uniform(0.0, 5.0)  # Generate a random salt

# TODO Lean's attempt
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


"""Task 3"""
file = open('passwords.txt', 'w')
file.flush()
file.write(hashed_password.hexdigest())  # String to write in file
file.close()

file = open('passwords.txt')
user_password_input = input("Enter Password: ")
password_to_compare = file.readline()
print(password_to_compare)

"""Task 5"""
# Read a string (pasword) from the keyboard input (ELLIOT) YUHANG Feng
final_password = input("")

# Call your hash function to verify the password
