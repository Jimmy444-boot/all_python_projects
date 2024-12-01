# Rollercoaster Ride Ticket Calculator

A simple Python program to calculate ticket prices for a rollercoaster ride based on height, age, and additional options like photos.

---

## Features
- Checks if the user meets the height requirement to ride.
- Calculates ticket prices based on age:
  - Children under 12: $5
  - Youth (12-18): $7
  - Adults: $12
  - Free rides for ages 45-55 as a special offer.
- Offers an optional photo feature for an additional $3.
- Displays the total bill based on selections.

---

## How It Works
1. The program prompts the user to enter their height in centimeters.
   - If the height is below 120 cm, the user cannot ride.
   - If the height is 120 cm or above, the program proceeds to calculate the ticket price.
2. Asks for the user's age to determine the ticket price.
3. Offers the option to include a photo for an additional $3.
4. Displays the total amount the user needs to pay.

---

## Usage

1. Save the script as `rollercoaster_calculator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the script using:

   ```bash
   python rollercoaster_calculator.py
