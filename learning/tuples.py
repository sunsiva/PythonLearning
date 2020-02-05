# Tuple: is basically kind of list but its immutable as we can not remove or add items etc . we have only 2 funtions count and index
'''numbers = (1, 2, 3)
print(numbers[0])

# Unpacking:
coordinates = (1, 2, 3)
x, y, z = coordinates #it assigns values to the individual variables
print(y)

# Dictionaries
customer = {
    "name": "Sun Siva",
    "age": "37",
    "is_verified": True
}

print(customer["name"])
print(customer.get("Age", "28")) # update the values when we get none object

# Exercise: print numbers in words
phone = input("Enter number")
number_in_words = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
}
output = ""
for no in phone:
    output += number_in_words.get(no, "!") + " "
print(output)
'''

# Convert message to emoji..
# to get a emoji keyboard shoartcut is press windows key along with semicolon(;)
message = input(">")
split_msg = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😒"
}
output = ""
for word in split_msg:
    output += emojis.get(word, word) + " "
print(output)
