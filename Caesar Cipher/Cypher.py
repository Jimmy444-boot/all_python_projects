# Import the logo art (assumed to be a variable from the 'art' module)
from art import logo
print(logo)  # Display the logo

# List of all lowercase alphabet letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Prompt the user to specify if they want to encode or decode
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

# Prompt the user to input their message
text = input("Type your message:\n").lower()

# Prompt the user to enter the shift number (key for the cipher)
shift = int(input("Type the shift number:\n"))


# Function to handle Caesar Cipher logic
def caesar_cipher(original_text, shift_number, encode_or_decode):
    output = ""  # Initialize an empty string to hold the result
    for letter in original_text:  # Loop through each letter in the input text
        if letter in alphabet:  # Check if the letter is in the alphabet list
            position = alphabet.index(letter)  # Get the index (position) of the letter in the alphabet

            # Shift the position based on the operation (encode or decode)
            if encode_or_decode == 'encode':
                position += shift_number  # Shift forward for encryption
            elif encode_or_decode == 'decode':
                position -= shift_number  # Shift backward for decryption

            # Ensure the position wraps around using modulo
            position %= len(alphabet)

            # Find the new letter after the shift and add it to the output string
            new_letter = alphabet[position]
            output += new_letter
        else:
            # If the character is not in the alphabet (e.g., space or punctuation), keep it unchanged
            output += letter

    # Print the final result of encoding or decoding
    print(f"Here is the {encode_or_decode}d result: {output}")


# Call the Caesar Cipher function with the initial user input
caesar_cipher(original_text=text, shift_number=shift, encode_or_decode=direction)

# Loop to ask the user if they want to restart or exit
should_continue = True
while should_continue:
    restart = input("Type 'yes' to continue, or 'no' to stop:\n").lower()

    if restart == 'no':  # Exit the loop if the user says 'no'
        should_continue = False
        print("Come again, cheers 🍻")  # Exit message
    else:
        # If the user chooses to continue, prompt for new inputs
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # Call the function again with new inputs
        caesar_cipher(original_text=text, shift_number=shift, encode_or_decode=direction)
