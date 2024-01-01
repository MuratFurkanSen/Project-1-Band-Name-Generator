# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
passwordDiff = input("Which difficulty would you like to choose(Easy or Hard):")
nr_letters = int(input("How many letters would you like in your password:"))
nr_symbols = int(input(f"How many symbols would you like:"))
nr_numbers = int(input(f"How many numbers would you like:"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
if passwordDiff.upper() == "EASY":
    for i in range(nr_letters):
        password += letters[random.randint(0, len(letters) - 1)]
    for i in range(nr_symbols):
        password += symbols[random.randint(0, len(symbols) - 1)]
    for i in range(nr_numbers):
        password += numbers[random.randint(0, len(numbers) - 1)]

elif passwordDiff.upper() == "HARD":
    password_len = nr_letters+nr_symbols+nr_numbers
    while len(password) < password_len:
        randChar = random.randint(0, 2)
        if randChar == 0 and nr_letters > 0:
            password += letters[random.randint(0, len(letters) - 1)]
            nr_letters -= 1
        elif randChar == 1 and nr_symbols > 0:
            password += symbols[random.randint(0, len(symbols) - 1)]
            nr_symbols -= 1
        elif randChar == 2 and nr_numbers > 0:
            password += numbers[random.randint(0, len(numbers) - 1)]
            nr_numbers -= 1
else:
    print("Choose a Valid Difficulty Level.")
print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
