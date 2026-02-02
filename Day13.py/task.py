# # import random
# # import maths

# # def mutate_number(a_list):
# #     b_list = []
# #     new_item = 0

# #     for item in a_list:
# #         new_item = item * 2
# #         new_item += random.randint(1, 3)
# #         new_item = maths.add(new_item, item)    
# #         b_list.append(new_item)
# #     print(b_list)

# # mutate_number([1,2,3,4,5])

# # def odd_or_even(number):
# #     if number % 2 == 0:
# #         return "This is an even number."
# #     else:
# #         return "This is an odd number."

# year = int(input("enter a year:"))

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# print(is_leap(year))

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])

fizz_buzz(15)

