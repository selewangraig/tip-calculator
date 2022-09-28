#This program will calculate the total bill to pay, which will include the tip as well.

#Total bill will be rounded off to 2dp

print("Welcome to the tip calculator")
bill = input("What was the total bill? $")

new_bill = float(bill)

p_tip = input("What percentage tip would you like to give? 10, 12 0r 15? ")

newp_tip = int(p_tip)

tip = new_bill * (newp_tip / 100)

total_bill = new_bill + tip

number_of_people = input("How many people to split the bill? ")

ppl = int(number_of_people)

split_bill = round(total_bill / ppl, 2)

message = f"Each person should pay: ${split_bill}"

print(message)