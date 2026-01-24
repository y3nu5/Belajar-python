# nested_dictionary = {
#     "list_name" : [["item1", "item2", "item3"], ["itemA", "itemB", "itemC"]]
# }

# print(nested_dictionary["list_name"][1][0])  # Output: itemA

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict[1] = 4

for key in dict:
    print(f"Key: {key}")
    value = dict[key]
    print(f"Key: {key}, Value: {value}")