import random
import string

replacement_dict = {}

for _ in range(5):
    while True:
        letter = input("Enter a lowercase character: ")
        if len(letter) == 1 and letter.islower():
            break
        print("Invalid input")

    replacement_set = set()
    while len(replacement_set) < 3:
        replacement = input(f"Enter a replacement for '{letter}': ")
        if len(replacement) == 1 and replacement not in replacement_set:
            replacement_set.add(replacement)
        else:
            print("Invalid or duplicate character. Try again. ")

    replacement_dict[letter] = list(replacement_set)

passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

categorized_passwords = {"Strong password": [], "Weak password": []}

for password in passwords:
    mod_password = list(password)
    replaced_count = 0

    index = 0
    while index < len(mod_password):
        char = mod_password[index]
        if char in replacement_dict:
            mod_password[index] = random.choice(replacement_dict[char])
            replaced_count += 1
        index += 1

    new_password = ''.join(mod_password)

    if replaced_count > 4:
        categorized_passwords["Strong password"].append(new_password)
    else:
        categorized_passwords["Weak password"].append(new_password)

print("\nGENERATED PASSWORDS:")

print("\nStrong passwords: ")
for pwd in categorized_passwords["Strong password"]:
    print(pwd)

print("\nWeak passwords: ")
for pwd in categorized_passwords["Weak password"]:
    print(pwd)
