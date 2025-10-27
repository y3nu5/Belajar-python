print("welcome to the rollercoaster")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("children ticket price is $5.")
    elif age >= 12 and age <= 18:
        bill = 7
        print("teenagers ticket price is $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("adult ticket price is $12.")

    takes_photo = bool(input("Do you want a photo taken? Y or N. "))
    if takes_photo is True:
        bill += 3
        print(f"your final bill is ${bill}")

else:
    print("Sorry, you need to be at least 120cm tall to ride.")
