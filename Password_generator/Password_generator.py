import random

# Lists of characters, numbers, and symbols to choose from for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+']

try:
    # Welcome message
    print("Welcome to the PyPassword Generator! 😊")

    # Get the number of letters, symbols, and numbers the user wants in their password
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like in your password?\n"))
    nr_numbers = int(input("How many numbers would you like in your password?\n"))

    # Ensure that the input is valid, i.e., greater than or equal to 1
    if nr_letters < 1 or nr_symbols < 1 or nr_numbers < 1:
        raise ValueError("Please enter a number greater than 1")

    # Initialize empty list to store the chosen characters
    password_in_list = []

    # Randomly select the specified number of letters and append to the list
    for letter in range(nr_letters):
        selected_letters = random.choice(letters)  # Randomly pick a letter from the list
        password_in_list.append(selected_letters)

    # Randomly select the specified number of symbols and append to the list
    for symbol in range(nr_symbols):
        selected_symbols = random.choice(symbols)  # Randomly pick a symbol from the list
        password_in_list.append(selected_symbols)

    # Randomly select the specified number of numbers and append to the list
    for number in range(nr_numbers):
        selected_numbers = random.choice(numbers)  # Randomly pick a number from the list
        password_in_list.append(selected_numbers)

    # Shuffle the list to ensure the password characters are in random order
    random.shuffle(password_in_list)

    # Convert the list into a string
    password = ""
    for item in password_in_list:
        password += str(item)  # Convert each item to a string and add it to the password string

    # Display the generated password
    print(f'Your generated 🔐password is {password}')

# Catch ValueErrors (for invalid input) and display the e
except ValueError as e:
    print(f"Error: {e}")