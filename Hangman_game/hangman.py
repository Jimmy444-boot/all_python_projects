import random
from hangman_art import stages, logo  # Import the hangman graphics and logo
from hangman_words import word_list  # Import the list of words for the game

# Randomly select a word for the game
chosen_word = random.choice(word_list)

# Create a display string for the chosen word, initially filled with '_'
invisible_chosen_word = "_" * len(chosen_word)

# Display the logo
print(logo)

# Initialize game variables
lives = 6  # Number of incorrect guesses allowed
game_over = False  # Game loop flag
correct_word = []  # List to store correctly guessed letters
print(chosen_word)  # Debugging: Show the word (remove in production)
print(f"Word to guess: {invisible_chosen_word}")

# Main game loop
while not game_over:
    display = ""  # Reset the display string for each round
    print(f'You have {lives} lives left.')
    guess = input("Guess a letter: ").lower()  # Get user input

    # Check if the letter has already been guessed
    if guess in correct_word:
        print(f"You have already guessed the letter '{guess}'. Try a different one.")

    # Update the display and correct_word list based on the guess
    for letter in chosen_word:
        if letter == guess:
            display += letter
            if letter not in correct_word:  # Avoid duplicate entries
                correct_word.append(letter)
        elif letter in correct_word:  # Show letters already guessed correctly
            display += letter
        else:
            display += "_"  # Fill in blanks for the rest of the letters

    # Print the current progress of the word
    print(f"Word to guess: {display}")

    # Deduct a life if the guess is not in the chosen word
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed the wrong letter, '{guess}' is not in the word. You lost a life.")
        if lives == 0:
            game_over = True
            print('You lose 💔. No lives left.')
            print(f"The correct word was: '{chosen_word}'")

    # Check if the player has guessed the entire word
    if "_" not in display:
        game_over = True
        print('You Win 🥇')

    # Print the current hangman stage
    print(stages[lives])
