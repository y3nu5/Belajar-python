import random
from art import higher_lower, vs
from game_data import data

def get_random_account():
    random_choice = random.choice(data)
    return (
        random_choice['name'],
        random_choice['followers'],
        random_choice['description'],
        random_choice['country']
    )

Current_score = 0
game_over = False

while not game_over:
    print(higher_lower)
    compare_A = get_random_account()
    print (f"Compare A: {compare_A[0]}, {compare_A[2]}, from {compare_A[3]}")
    print(vs)
    compare_B = get_random_account()
    print (f"Compare B: {compare_B[0]}, {compare_B[2]}, from {compare_B[3]}")

    guess = str(input("who more followers? Type A or B"))

    if guess == "A":
        if compare_A[1] > compare_B[1]:
            Current_score += 1
            print(f"You're right! Current score: {Current_score}")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {Current_score}")
    else:
        if compare_B[1] > compare_A[1]:
            Current_score += 1
            print(f"You're right! Current score: {Current_score}")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {Current_score}")

    
        
