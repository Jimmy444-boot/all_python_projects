print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
cross_direction = input("Your are at a cross road. Where do you want to go? \n    "
                        "Type 'left' or 'right' \n")
if cross_direction.lower()  == 'left':
    lake_direction = input("You have come to a lake. There is an island in the middle of the lake \n    "
                        "Type 'wait' to wait for a boat. Type 'swim' to swim across \n")
    if lake_direction.lower()  == "wait":
       door_choice = input("You have arrived at the island unharmed. There is a house with 3 doors."
              "One red, one yellow and one blue. Which color do you choose? \n")

       if door_choice.lower() == "blue":
            print("You Win! 🏆")
       else:
            print("Game over, you have chosen the wrong door")
    else:
        print("Game over, you have been bitten by a shark 🦈")

else:
    print("Game Over, you have been hit by a car 💀.")