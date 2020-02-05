# for item in "Python":
# for item in range(10):
# for item in [1, 2, 3, 4, 5, 6]:
# for item in range(5, 10, 2):  # in range 2 param is 2 steps forward in the range so the result is 5,7,9
#    print(item)

# Exercise 1: count all the items in the shopping cart
"""prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total price is {total}")
"""

# Exercise 2 : Type 1: Print like F shape with X
"""shape = [5, 2, 5, 2, 2]
for item in shape:
    print(item * "X")
"""
# Exercise 2 : Type 2: Print like F shape with X
"""shape = [5, 2, 5, 2, 2]
for x_count in shape:
    output = ""
    for y in range(x_count):
        output += "X"
    print(output)
"""
# Exercise 3: Type 1: Find the the largest number in the list
'''lists = [2, 4, 8, 6, 10]
lists.sort(reverse=True) # or lists.reverse() 
lists.sort()
print(lists[-1])
'''
# Exercise 3: Type 2: Find the the largest number in the list
'''numbers = [3,2,6,9,10,15,3]
max=numbers[0]
for no in numbers:
    if no > max:
        max=no
print(max)
'''
# Exercise 4: 2D list
'''numbers = [5, 4, 3, 20, 8 ,20]
numbers.append(50) # append at the end of the list
numbers.insert(0,25) # insert at the beginning of the list
numbers.remove(3) # removes the value in the list
#numbers.clear() # clears the entire list
numbers.pop() # it removes at the last item in the list
print(numbers)
'''
# Exercise 5:Type 1 Remove the duplicates in a list
numbers = [5, 4, 3, 20, 8, 20, 5]
for item in numbers:
    if(numbers.count(item)>1):
        numbers.remove(item)
print(numbers)
# Exercise 5:Type 2 Remove the duplicates in a list
numbers = [5, 4, 3, 20, 8, 20, 5]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)



