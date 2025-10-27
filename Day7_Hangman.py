import random
lists = ["camel", "horse"]

word = random.choice(lists)
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
    guess_a_letter = input("Guess a letter: ").lower()

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
            print(display)
            correct_guesses.append(guess_a_letter)
            print(correct_guesses)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")


    



