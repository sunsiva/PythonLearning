"""
def greet_user(name):
    print(f"Hello {name}!!")
    print("Welcome aboard")


print("Start")
greet_user("siv")
print("Finish")


# Function with return values
def square(number):
    return number * number


print(square(21))
"""
'''
# Function with emoji project
def emoji_converter(message):
    split_msg = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for word in split_msg:
        output += emojis.get(word, word) + " "
    return  output


message = input(">")
print(emoji_converter(message))
'''

# A call from utilis

import utilis # this is one way of importing modules

my_list=[12,3,5,2,5,55,0]
find_max_no = utilis.find_max(my_list)
print(find_max_no)

from utilis import find_max # this is another way of importing directly functions in the modules
my_list=[12,3,5,2,5,25,0]
print(find_max(my_list))