# Password Generator - This code helps a user to generate passwords of desired number of letters, numbers, and symbols
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator\n")
# Ask the user the number of letters, numbers, and symbols
num_letters = int(input("How many letters of the alphabet do you want to generate: "))
num_numbers = int(input("How many numbers do you want to generate: "))
num_symbols = int(input("How many symbols do you want to generate: "))

# Randomly generate the letter segment of the password based on the number of desired letters
letters_password = ""
for num in range(num_letters):
    letters_password += random.choice(letters)

# Randomly generate the number segment of the password based on the number of desired numbers
numbers_password = ""
for num in range(num_numbers):
    numbers_password += random.choice(numbers)

# Randomly generate the symbol segment of the password based on the number of desired symbols
symbols_password = ""
for num in range(num_symbols):
    symbols_password += random.choice(symbols)

# Combine the random letters, numbers, and symbols to form a single string
password = letters_password + numbers_password + symbols_password

# Turn the generated password to a list and reshuffle
list_ = list(password)
random.shuffle(list_)  # Reshuffle the password list
generated_password = ''.join(list_)
print(generated_password)
