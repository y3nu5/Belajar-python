print("welcome to the pizza deliveries!")

size = input("what is your pizza size ? S, M, or L")
papperoni = input("Do you want pepperoni? Y or N.")
extra_cheese = input("Do you want extra cheese? Y or N.")

bill = 0

if size == "S":
   bill = 15
elif size == "M":
   bill = 20
elif size == "L":
   bill = 25
else:
   print("no sell pizza size")

if papperoni == "Y":
   if size == "S":
      bill +=2
   else:
      bill +=3

if extra_cheese == "Y":
   bill += 1


print(f"your final bill is ${bill}")

