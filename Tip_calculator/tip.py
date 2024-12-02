# Welcome message for the tip calculator
print("Welcome to the tip calculator!")

# Ask for the total bill (without tip)
total_bill_without_tip = float(input("What was the total bill? "))

# Ask for the percentage of the bill as a tip (10, 12, or 15)
perc_of_bill_as_tip = float(input("How much tip would you like to give? 10, 12, or 15? ")) / 100

# Ask for the number of people to split the bill
num_of_people_to_pay = int(input("How many people should I split the bill for? "))

# Calculate the tip amount based on the percentage
tip_perc = total_bill_without_tip * perc_of_bill_as_tip

# Calculate the total bill including the tip
total_bill_and_tips = total_bill_without_tip + tip_perc

# Calculate the amount each person should pay
bill_per_person = total_bill_and_tips / num_of_people_to_pay

# Print the final result, rounded to 2 decimal places for clarity
print(f"Each person should pay: ${bill_per_person:.2f}")
