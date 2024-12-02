# Welcome message
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

# First choice at the crossroad
cross_direction = input("You are at a crossroad. Where do you want to go? \n    "
                        "Type 'left' or 'right' \n").lower()

if cross_direction == 'left':
    # Second choice at the lake
    lake_direction = input("You have come to a lake. There is an island in the middle of the lake. \n    "
                           "Type 'wait' to wait for a boat. Type 'swim' to swim across \n").lower()

    if lake_direction == "wait":
        # Third choice for the doors
        door_choice = input("You have arrived at the island unharmed. There is a house with 3 doors. "
                            "One red, one yellow, and one blue. Which color do you choose? \n").lower()

        # Winning condition
        if door_choice == "blue":
            print("You Win! 🏆")
        else:
            print("Game over, you have chosen the wrong door.")
    else:
        print("Game over, you have been bitten by a shark 🦈.")
else:
    print("Game Over, you have been hit by a car 💀.")
