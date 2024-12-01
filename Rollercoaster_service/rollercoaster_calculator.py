
#Rollercoaster Ride Ticket Calculator
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    # Determine ticket price based on age
    if age < 12:
        ticket_price = 5
        print("Child tickets are $5.")
    elif age <= 18:
        ticket_price = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:  # Free tickets for middle-aged riders
        ticket_price = 0
        print("Everything is going to be okay. Have a free ride on us!")
    else:
        ticket_price = 12
        print("Adult tickets are $12.")

    # Optional photo
    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo.upper() == "Y":
        ticket_price += 3
        print("Adding $3 for the photo.")

    print(f"Your final bill is ${ticket_price}\n Have fun.")
else:
    print("Sorry, you have to grow taller before you can ride.")
