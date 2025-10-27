import random
import sys

rock = '''
    -----
---'-----)
    -----
rock
'''

paper = '''
-----
    -----
    -----
    -----
-----
paper
'''

scissors = '''
 ----
 ----
 scissors
'''

union = [rock, paper, scissors]

Choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if Choice == "0":
    print(rock)
elif Choice == "1":
    print(paper)    
elif Choice == "2":
    print(scissors)
else:
    print("You typed an invalid number, you lose!")

computer_choice = random.choice(union)
print("Computer chose:", computer_choice)

# logic if user take rock
if Choice == "0" and computer_choice == paper:
    print("You lose!")
elif Choice == "0" and computer_choice == scissors:
    print("You win!")
elif Choice == "0" and computer_choice == rock:
    print("It's a draw!")
# logic if user take paper
elif Choice == "1" and computer_choice == rock:
    print("You win!")
elif Choice == "1" and computer_choice == scissors:
    print("You lose!")
elif Choice == "1" and computer_choice == paper:
    print("It's a draw!")
# logic if user take scissors
elif Choice == "2" and computer_choice == rock:
    print("You lose!")
elif Choice == "2" and computer_choice == paper:
    print("You win!")
elif Choice == "2" and computer_choice == scissors:
    print("It's a draw!")
else:
    sys.exit()