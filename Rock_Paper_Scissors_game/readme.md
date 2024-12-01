readme_content = """
# Rock, Paper, Scissors Game - README

## Introduction
This is a simple **Rock, Paper, Scissors** game implemented in Python. The user plays against the computer by selecting one of three options: Rock, Paper, or Scissors. The game determines the winner based on the classic rules:

- Rock beats Scissors
- Scissors beat Paper
- Paper beats Rock
- If both selections are the same, it's a tie.

---

## Prerequisites
Before running the game, ensure the following are installed:

1. **Python 3.6+**
2. A custom module named `ascii_art` that defines `rock`, `paper`, and `scissors` as ASCII art representations of each choice.

---

## How to Play
1. Run the Python script.
2. The game will prompt you to:
   > "Select a number between 0 to 2, 0 for Rock, 1 for Paper, and 2 for Scissors."
3. Enter your choice as a number:
   - `0` for Rock
   - `1` for Paper
   - `2` for Scissors
4. The game will:
   - Display your choice and the computer's choice in ASCII art.
   - Announce the winner.

---

## Script Logic
1. **Imports**:
   - `ascii_art`: Provides ASCII representations of Rock, Paper, and Scissors.
   - `random`: Used for the computer to randomly pick a choice.

2. **Game Flow**:
   - The user inputs a number (`0`, `1`, or `2`).
   - The user's input is validated to ensure it is within range. Invalid inputs are handled gracefully.
   - The user's and computer's choices are displayed.
   - The winner is determined based on the rules:
     - Rock beats Scissors.
     - Paper beats Rock.
     - Scissors beat Paper.
     - Ties are announced when both choices are the same.

3. **Error Handling**:
   - Invalid inputs (e.g., numbers outside `0-2` or non-numeric input) trigger an error message and gracefully exit the game.

---

## Example Run

```plaintext
Welcome to the Rock, Paper, Scissors game
Select a number between 0 to 2, 0 for Rock, 1 for Paper, and 2 for Scissors: 1

Your choice:
(paper ASCII art)

Computer's choice:
(rock ASCII art)

You Win 🏆
