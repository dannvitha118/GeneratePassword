# -*- coding: utf-8 -*-
"""Generate Password.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Syjn-Hn4dfaXDeOeyTLmSiTbeNy7Gypz
"""

import random
import string

# Function to generate password
def generate_password(length, include_letters, include_numbers, include_symbols):
    # Initialize possible characters based on user preferences
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Ensure there's at least one type selected
    if not characters:
        return "You must select at least one character type (letters, numbers, or symbols)."

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to interact with user via Colab widgets
def main():
    from google.colab import widgets

    # User inputs
    length = int(input("Enter the desired password length: "))
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate and display the password
    password = generate_password(length, include_letters, include_numbers, include_symbols)
    if isinstance(password, str):
        print(f"Your generated password is: {password}")

# Call the main function
main()