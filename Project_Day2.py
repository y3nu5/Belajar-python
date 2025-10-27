print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
amount_people = int(input("How many people to split the bill? "))

tip = total_bill * (percentage_tip / 100)
total_amount = total_bill + tip
amount_per_person = total_amount / amount_people

Final_Amount = round(amount_per_person, 2)

print(f"Each person should pay: ${Final_Amount}")