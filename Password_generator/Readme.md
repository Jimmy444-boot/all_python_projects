# PyPassword Generator

## Description

The **PyPassword Generator** is a simple Python program that generates a random password based on user input. The program allows the user to specify how many letters, symbols, and numbers they want in their password. It then randomly selects characters from predefined lists of letters, symbols, and numbers to create a password. This password can be used for various applications or websites requiring secure passwords.

## Features
- Allows the user to specify the number of letters, symbols, and numbers for the password.
- Randomly selects characters from a list of uppercase, lowercase letters, numbers, and symbols.
- Validates user input to ensure the numbers are greater than or equal to 1.
- Combines letters, symbols, and numbers to generate a secure password.

## Requirements
- Python 3.x
- No external libraries required (only the built-in `random` module).

## How to Use

1. **Run the script**:
    - Open a terminal or command prompt.
    - Navigate to the folder where the script is saved.
    - Run the Python script using the command:
      ```bash
      python py_password_generator.py
      ```

2. **Provide input**:
    - The script will prompt you to enter the number of:
      - Letters
      - Symbols
      - Numbers
    - Enter a number for each prompt. The number should be greater than or equal to 1.
    
3. **Password generation**:
    - After entering the inputs, the program will generate a password containing the specified number of letters, symbols, and numbers, and print the generated password.

## Example

```bash
Welcome to the PyPassword Generator! 😊
How many letters would you like in your password?
8
How many symbols would you like in your password?
3
How many numbers would you like in your password?
2
Your generated 🔐password is Rm!t6W@3
