#this is  working
print(15 % 5)
print(14 % 5)
print(13 % 5)
print(12 % 5)
print(11 % 5)
print(10 % 5)
print(9 % 5)
print(5 % 3)


car_name = "Weibe Mobile"
car_type = "Nissan GTR"
car_cylinders = 8
car_mpg = 9000.1

# Inline printing
print("I have a car called the %s" % car_type)

# Function


def print_hw():
    print('Hello World"')


print_hw()
print_hw()
print_hw()

def say_hi(name): # nameis a premeter
    print('Hello ')

say_hi("Jimmy")


def print_age(name, age):
    print("%s is %d years old" % (name, age))


# if statement



def f(x):
     return x**3 +4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))



def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage < 90 and percentage >=80 :
        return "8"
    elif percentage >= 70 :
        return "c"


'''Write a function called "happy_bday"
that "sings" (prints) Happy birthday

It must take one permeter called "name"
'''

def happy_bday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday to %s" % name)
    print("Happy birthday to you")

happy_bday ('john')


# Loops

for num in range(10):
    print(num + 1)

# DO NOT RUN !!
a = 1
while True:
    print (a)


    # Random Numbers

import random   # This Should be on line 1
print(random,randit(0, 100)
