import random
from Word_List import random_words 
from hangmanart import stages, welcome

lives = 6

print(welcome)

word = random.choice(random_words)
print(word)

# Create Placeholders
# versi 1
# placeholders = []
# for letter in word:
#     placeholders.append("_")

# print(" ".join(placeholders))

placeholder = ""
for letter in range(len(word)):
    placeholder += "_"
print(placeholder)

# Ask the user to guess a 
game_over = False
correct_guesses = []

while not game_over:

    print(f"Lives left: {lives}")
    guess_a_letter = input("Guess a letter: ").lower()

    if guess_a_letter in correct_guesses:
        print(f"You've already guessed the letter '{guess_a_letter}'. Try again.")

    display = ""


# for letter in placeholders:
#     if letter == guess_a_letter:
#        placeholders = guess_a_letter

# -- versi 1
# for i in range(len(word)):
#     if word[i] == guess_a_letter:
#         placeholders[i] = guess_a_letter  # Ganti garis bawah dengan huruf yang benar
# print(" ".join(placeholders))

    # -- versi 2
    for letter in word:
        if letter == guess_a_letter:
            display += letter
            correct_guesses.append(guess_a_letter)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    print(display)

    if guess_a_letter not in word:
        lives -=1

    if lives == 0:
        game_over = True
        print("************* You lose *************")

    if "_" not in display:
        game_over = True
        print("************* You win *************")

    print(stages[lives])


    



