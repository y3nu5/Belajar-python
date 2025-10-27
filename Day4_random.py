import random
# import tes_module

# random_integer = random.randint(1, 100)
# print ("angka acak:", random_integer)
# print("angka favorit:", tes_module.favourite_number)

# random_floating_point = random.uniform(1, 100)
# print("angka floating point:", random_floating_point)

# random_choice = random.choice(["Tails", "Heads"])
# print("koin pilihan:", random_choice) 

random_integer = random.randint(0,1)
if random_integer == 1:
    print("koin pilihan: Heads")
elif random_integer == 0:
    print("koin pilihan: Tails")
else :
    print("error")
