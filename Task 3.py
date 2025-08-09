import random
import string

# Step 1: Ask user for password length
length = int(input("Enter the desired password length: "))

# Step 2: Ask user what to include in the password
include_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

# Step 3: Create character pool based on user input
characters = ''
if include_letters:
    characters += string.ascii_letters
if include_digits:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

# Step 4: Validate selection
if not characters:
    print("Error: Please select at least one character type (letters, digits, or symbols).")
else:
    # Step 5: Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\nGenerated Password:", password)
