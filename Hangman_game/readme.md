# Hangman Game

Welcome to the **Hangman Game**! This classic word-guessing game challenges players to uncover a hidden word by guessing one letter at a time. Be careful, though—each incorrect guess brings you closer to the gallows!

## How It Works
- The game selects a random word from a predefined list.
- Players have 6 lives (incorrect guesses) to reveal the word.
- With each correct guess, letters are revealed.
- If you run out of lives before guessing the word, you lose.

---

## Features
- **Random Word Selection:** The word is randomly chosen from a word list.
- **Dynamic Display:** The game updates the word display after every guess.
- **Graphics and Stages:** Includes visual stages of the hangman using ASCII art.
- **Replayability:** Offers a fun and challenging experience every time.

---

## Requirements
- Python 3.x installed on your system.
- Two additional Python files:
  1. **`hangman_art.py`:** Contains the stages and logo.
  2. **`hangman_words.py`:** Contains the list of words.

---

## File Structure
Ensure the following files are in the same directory:
**`hangman_art.py`:** 
**`hangman_words.py`:**

## How to Play
1. Setup:
   Clone or download the repository.
   Ensure all three files (main.py, hangman_art.py, hangman_words.py) are in the same directory.

2. Run the Game: python main.py

3. Gameplay
   * Follow the prompts to guess letters.
   * Watch the hangman art evolve with incorrect guesses.
   * Guess the word correctly to win or lose if the hangman is fully drawn!

## Example Gameplay
Welcome to the Hangman Game!
Word to guess: _ _ _ _ _
Guess a letter: a
Word to guess: _ a _ _ _
You have 5 lives left.
Guess a letter: e
You guessed the wrong letter, 'e' is not in the word. You lost a life.
You lose 💔. No lives left.
The correct word was: 'apple'




