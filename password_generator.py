"""
    Password Generator Project
    input:  password length
            Number of Digits
            Number of Symbols
    
    output: password (as string)
"""

# importing the relevant modules
import string
import random

# List of all lowercase and uppercase characters in Python
all_alphabets = list(string.ascii_letters)
all_digits = list(string.digits)
all_symbols = list(string.punctuation)

# Ask user for how many letters they would like in their password and cast to integer
no_of_letters = int(input('How many letters would you like in your password? '))

# Ask user for how many symbols they would like in their password and cast to integer
no_of_symbols = int(input('How many symbols would you like in your password? '))

# Ask user for how many digits they would like in their password and cast to integer
no_of_digits = int(input('How many numbers would you like in your password? '))

# Set Accumulator for Password Characters List
password_characters_list = []

# Get the random letter for the password
# Randomly Select the characters
for number in range(no_of_letters):
#       select a random characer from list of alphabets and append to the password characters list 
    random_letters = random.choice(all_alphabets)
    password_characters_list.append(random_letters)
print(password_characters_list)

# Set Accumulator for the Number of Symbols List
password_symbols_list = []

# Get the Random Symbols for the password symbols
# Randomly Select the characters
for number in range(no_of_symbols):
#       select a random symbol from list of symbols and append to the password symbols list 
    random_symbols = random.choice(all_symbols)
    password_symbols_list.append(random_symbols)
print(password_symbols_list)

# Set Accumulator for the Number of Digits List
password_digits_list = []

# Get the Random Digits for the password
# Randomly Select the characters
for number in range(no_of_digits):
#       select a random digit from list of digits and append to the password digits list 
    random_digits = random.choice(all_digits)
    password_digits_list.append(random_digits)
print(password_digits_list)
    
# Add the lists to get the final_password_list and shuffle the final_password_list
final_password_list = password_characters_list + password_symbols_list + password_digits_list
random.shuffle(final_password_list)
print(final_password_list)

# Now that we have our password in a list lets change that to a string then print it
# Accumulator for string_password
string_password = []

for character in final_password_list:
#       Append the character to the string_password
    string_password.append(character)

# Print the string password
print('Your password is: ' + ''.join(string_password))