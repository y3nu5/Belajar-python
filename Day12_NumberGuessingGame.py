import random

choice_number = random.choice(range(1, 101))
print(choice_number)

Attempts = 0
Game_Over = False

print ("Welcome the number guessing game!\n I'm thinking of a number between 1 to 100")


Difficult = input(f"Choose a difficulty. Type 'easy' or 'hard' : ")
if Difficult == 'easy':
    Attempts += 10
    print("You have 10 attempts remaining to guess the number")

else:
    Attempts += 5
    print("You have 5 attempts remaining to guess the number")

while not Game_Over:
    Guess = int(input("Make a guess : "))

    if Guess == choice_number:
        print("You got it, you winn")
        Game_Over = True
        exit()
    elif Guess < choice_number:
        print("Too low")
        Attempts -= 1
        print(f"you have {Attempts} attempts remaining to guess the number")
    else:
        print("too high")
        Attempts -= 1
        print(f"you have {Attempts} attempts remaining to guess the number")

    if Attempts == 0:
        print("you've run out of guesses, you lose")
        Game_Over = True