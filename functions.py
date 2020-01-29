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

# Function
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
