
from ascii_art import rock, paper, scissors
import random


selection = [rock, paper, scissors]
print("Welcome to the Rock, Paper, Scissors game")

try:
    rps_picking = int(input("select a number between 0 to 2, 0 for rock, 1 for paper and 2 for scissors "))
    if rps_picking < 0 or rps_picking > 2:
        raise ValueError("Invalid choice. Please select 0, 1, or 2.")

    human_choice = selection[rps_picking]
    computer_choice = selection[random.randint(0, 2)]

    print(f"Your choice{human_choice}")
    print(f"Computer's choice{computer_choice}")

    if human_choice == rock and computer_choice == scissors:
        print("You Win 🏆")
    elif human_choice == paper and computer_choice == scissors:
        print("Computer Wins, you loose 🤙")
    elif computer_choice == rock and human_choice == scissors:
        print("Computer Wins, you loose 🤙")
    elif human_choice == computer_choice:
        print("It's a tie")
    else:
        print("You Win 🏆")

except ValueError as e:
    print(f"Oops: {e}")

