# year = int(input("whats the year you were born? "))

# if year >= 1980 and year <= 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")
try:
    age = int(input("How old are you? "))
except ValueError:
    print("you have typed a an invalid age. please truy agin with a numerical value")
    age = int(input("How old are you? "))
if age >= 18:
    print(f"You can drive at age {age}.")