# Caesar Cipher Program 🛡️🔐

This is a Python program that implements the **Caesar Cipher** for **encryption** and **decryption** of messages. The program shifts each letter of a given message forward or backward in the alphabet by a user-specified number.

---

## Features ✨

- **Encrypt** a message by shifting letters forward in the alphabet.
- **Decrypt** a message by shifting letters backward in the alphabet.
- Handles non-alphabetic characters (like spaces and punctuation) without modification.
- Allows continuous operation until the user chooses to exit.

---

## How It Works 🛠️

The Caesar Cipher is a simple encryption technique where each letter in the input message is replaced by another letter **shifted a certain number of positions** in the alphabet.

For example, with a shift of `3`:
- `a` → `d`
- `b` → `e`
- `z` → `c` (it wraps around the alphabet)

---

## Code Example 🐍

Here is the Python code for the Caesar Cipher program:

```python
# Caesar Cipher Implementation
from art import logo  # Import a logo for styling (optional, if you have a separate art file)

print(logo)  # Display the logo

# Define the alphabet
alphabet = [chr(i) for i in range(97, 123)]  # Generate 'a' to 'z' using ASCII values

# Function to perform Caesar Cipher encryption/decryption
def caesar_cipher(text, shift, operation):
    result = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)  # Find the current position of the letter
            if operation == "encode":
                new_position = (position + shift) % 26  # Shift forward
            elif operation == "decode":
                new_position = (position - shift) % 26  # Shift backward
            result += alphabet[new_position]  # Add the shifted letter to the result
        else:
            result += letter  # Add non-alphabet characters unchanged
    print(f"The {operation}d result is: {result}")

# User input
while True:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar_cipher(text, shift, direction)

    # Ask user if they want to continue
    restart = input("Type 'yes' to go again or 'no' to exit: ").lower()
    if restart == "no":
        print("Goodbye! 🔐")
        break
