# Import necessary modules
from ascii_art import rock, paper, scissors  # Assuming rock, paper, scissors are ASCII art representations of the items
import random  # For generating random choices

# Create a selection list with the possible choices
selection = [rock, paper, scissors]

# Print a welcome message
print("Welcome to the Rock, Paper, Scissors game")

try:
    # Get the player's choice input and validate it
    rps_picking = int(input("Select a number between 0 to 2, 0 for rock, 1 for paper, and 2 for scissors: "))

    # Check if the input is within the valid range
    if rps_picking < 0 or rps_picking > 2:
        raise ValueError("Invalid choice. Please select 0, 1, or 2.")

    # Map the player's choice to the corresponding item (rock, paper, or scissors)
    human_choice = selection[rps_picking]

    # Generate the computer's random choice
    computer_choice = selection[random.randint(0, 2)]

    # Display both choices
    print(f"Your choice: {human_choice}")
    print(f"Computer's choice: {computer_choice}")

    # Determine the result of the game
    if human_choice == rock and computer_choice == scissors:
        print("You Win 🏆")
    elif human_choice == paper and computer_choice == scissors:
        print("Computer Wins, you lose 🤙")
    elif computer_choice == rock and human_choice == scissors:
        print("Computer Wins, you lose 🤙")
    elif human_choice == computer_choice:
        print("It's a tie")
    else:
        print("You Win 🏆")

# Catch the ValueError exception if the user inputs an invalid choice
except ValueError as e:
    print(f"Oops: {e}")
