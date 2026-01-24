def format_name(first_name, last_name):
    ''''Takes a first and last name and formats it to return 
    the title case version of the name.'''
    if first_name == "" or last_name == "":
        return "You did not provide the values"
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    print(f"{formatted_first_name} {formatted_last_name}")

format_name("john", "doe")

# def tes():
#     return 3*2

# output = tes()
# print(output)


# def teks(text):
#     return text+text

# def teks2(text1):
#     return text1.title()

# output = teks2(teks("hello"))
# print(output)