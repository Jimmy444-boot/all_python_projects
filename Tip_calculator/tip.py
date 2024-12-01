print("Welcome to the tip calculator!")
total_bill_without_tip = float(input("What was the total bill? "))
perc_of_bill_as_tip = float(input("How much tip would you like to give? 10,12,or 15? ")) /100
num_of_people_to_pay = int(input("How many people should I split the bill for? "))
tip_perc = total_bill_without_tip * perc_of_bill_as_tip
total_bill_and_tips = total_bill_without_tip + tip_perc
bill_per_person = total_bill_and_tips/num_of_people_to_pay
print("Each person should pay: ", bill_per_person)