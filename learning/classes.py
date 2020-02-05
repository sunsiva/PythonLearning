# Class
'''
class Point:
    def __init__(self, x, y): #this is the constructor called before other methods are called.
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point(10, 20)
point1.x = 10
point1.y = 20
print(point1.x)
point1.move()

point2 = Point(50, 100)
point2.x = 1
print(point2.x)
'''

# Exercise 2
'''
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"hey, i am {self.name} here")


p = Person("siva")
p.talk()

p2=Person("Myla")
p2.talk()
'''

# Interface
class Mommol:
    def walk(self):
        print("walk")

class Dog(Mommol):
    def dog_bark(self):
        print("dog barking")

class Cat(Mommol):
    def cat_miam(self):
        print("cat miaming")

cat1 = Cat()
cat1.cat_miam()