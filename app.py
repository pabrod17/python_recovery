import math



#Toogle Panel Visibility -> Open and hide the panel
# //////////////////////////////////////
print("Pablo Rodriguez")
print("o----")
print(" ||||")
print("*" * 10)

price = 10
price = 20
rating = 4.9
name = 'Pablo'
is_published = False

full_name = "John Smith"
age = 20
is_new = True
# //////////////////////////////////////
# print(price)
# #Receive input from user
# name = input("What is your name? ")
# print("Hi " + name)
# color = input("What is your favorite color? ")
# print(name + " likes " + color)
# //////////////////////////////////////
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2025 - int(birth_year)
# int()
# bool()
# float()
# print(age)
# //////////////////////////////////////
# weight_lbs = input("Weight (lbs): ")
# weight_kg = float(weight_lbs) * 0.454
# print("Weight (kg): " + str(weight_kg))
# course = "Python' for Beginners"
# course2 = 'Python for "Beginners'
# print(course)
# print(course2)
# another = course2[:]
# print(course2[:])
# print(another)
# //////////////////////////////////////
# course3 = ''' 
# Hi John,
# Here is our first email to you.
# Thank you,
# The support team
# '''
# print(course3)
# //////////////////////////////////////
# name = 'Jennifer'
# print(name[1:-1])
# //////////////////////////////////////

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] ' + 'is a coder'
# msg = f'{first} [{last}] is a coder'
# print(msg)
# //////////////////////////////////////
# course = 'Python for Beginners'
# print(course.lower())
# print(len(course))

# #Methods find,replace,....
# print(course.find('Beginners'))
# print(course.title())
# print(course.replace('Beginners', 'Absolute Beginners'))
# print(course)

# print('Python' in course)
# //////////////////////////////////////
# print(10 // 3 )
# print(10 / 3 )
# print(10 % 3 )
# print(10 ** 3 )

# x = 10
# x = x + 5
# x += 5
# print(x)

# y = 2.9
# print(round(-y))
# print(abs(-y))
# //////////////////////////////////////

# math.ceil(12.9)

# math.floor(12.9)
# //////////////////////////////////////
# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")
# //////////////////////////////////////
# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print('Down Payment:', down_payment)
# print(f'Down Payment: ${down_payment}')
# print(f'hola {down_payment}')
# //////////////////////////////////////

# has_high_income = True
# has_good_credit = True

# if has_high_income and not has_good_credit:
#     print('Eligible for loan')
# if has_high_income or has_good_credit:
#     print('Eligible for loan')

# //////////////////////////////////////

# temperature = 30
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# name = 'Alejandrodsfafasdfasdfasdfasfasdfasdfdasfasfsfsdfaerfqer4fqwe4rfe4arfeqw4rf3we4qrf'
# if len(name) < 3:
#     print('Name must be at least 3 characters')
# elif len(name) > 50:
#     print('Name must be a maximum of 50 characters')
# else:
#     print('Name looks good!')

# //////////////////////////////////////
# weight = float(input('Weight:'))
# unit = input('(L)bs or (K)g:')
# # if unit == 'l' or unit == 'L':
# if unit.upper == 'L':
#     converted = weight * 0.45
#     print(f'You are {converted} pounds')
# elif unit == 'k' or unit == 'K':
#     converted = weight / 0.45
#     print(f'You are {converted} kilos')
# //////////////////////////////////////
#as long as this condition is true
#as long as == while
#we'll jump out of this loop
# i = 1
# while i <= 5:
#     print('*' * i)
#     i +=1
# print('Done')

# //////////////////////////////////////
# secret_number = 0
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print('Sorry, you failed!')
# //////////////////////////////////////


# started = False
# while True:
#     command = input('>').lower()
#     if (command == 'help'):
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#               ''')
#     elif (command == 'start'):
#         if started:
#             print('Car is already started!')
#         else:
#             started = True
#             print("Car started... Ready to go!")
#     elif (command == 'stop'):
#         if not started:
#             print('Car is already stopped!')
#         else:
#             started = False
#             print('Car stopped.')
#     elif (command == 'quit'):
#         break
#     else: 
#         print("I don't understand that...")
# //////////////////////////////////////
# for item in 'Python':
#     print(item)
# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)
# for item in [1,2,3,4,5]:
#     print(item)
# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30.5]
# sum = 0
# for item in prices:
#     sum += item
# print(f'Total cost: {sum}')
# //////////////////////////////////////
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')


# numbers = [5, 2, 5, 2, 2]
# output = ''
# for item in numbers:
#     output = ''
#     for y in range(item):
#         output +='x'
#     print(output)
# //////////////////////////////////////
# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[-2])
# print(names[2:])
# print(names[2:4])
# print(names[:])
# names[0] = 'Hola'
# print(names)

# names = ['John', 'Bob', 'MaryStreet', 'Sarah', 'Mosh']
# # names.sort(key=len)
# # print(names[-1])

# longest_name = ''
# for item in names:
#     if len(item) > len(longest_name):
#         longest_name = item
# print(f'Longest name: {longest_name}')


# numbers = [3, 6, 2, 10, 4, 8]
# max = numbers[0]
# for item in numbers:
#     if item > max:
#         max = item
# print(f'Maximum number: {max}')


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][1] = 30
# print(matrix[0][1])
# print(matrix)
# for row in matrix:
#     for column in row:
#         print(column)


# numbers = [5, 2, 5, 7, 4]
# # numbers.append(20)
# # numbers.insert(0,60)
# # numbers.remove(2)
# # numbers.clear()
# numbers.pop()
# print(numbers.index(7))
# print(numbers)
# print(50 in numbers)#Return a boolean value
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# numbers.append(500)
# print(numbers)
# print(numbers2)


# numbers = [5,3,6,1,6,6,435,6]
# numbers_copy = []
# for item in numbers:
#     if not item in numbers_copy:
#         numbers_copy.append(item)
# print(numbers_copy)
    
# //////////////////////////////////////
#tuples
# numbers = (1, 2, 3)
# numbers[0] = 10
# print(numbers[0])
# //////////////////////////////////////
# coordinates = [1, 2, 3]
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# x, y, z = coordinates
# print(y)
# //////////////////////////////////////
#Dictionaries

# customer = {
#     'name' : 'John Smith',
#     'age' : 30,
#     'is_verified' : True
# }
# customer['name'] = 'New Name'
# customer['birthdate'] = 'Jan 2 2000' #Add new key-value
# print(customer['name'])
# print(customer.get('age'))
# print(customer.get('hola', 'Jan 1 1980'))
# print(customer)
# //////////////////////////////////////
# numbers = {
#     '0': 'zero',
#     '1': 'one', 
#     '2': 'two',
#     '3': 'three',
#     '4': 'four',
#     '5': 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine'
# }
# item = input('Phone:')
# outpout = ''
# for char in item:
#     outpout += numbers.get(char, '!') + ' '

# print(f'Result: {outpout}')


# message = input('> ')
# words = message.split(' ')
# emojis = {
#     ':)': '😊',
#     ':(': '😔',
#     ':D': '😃',
#     ':P': '😛',
#     '<3': '❤️'
# }
# output = ''
# for word in words:
#     output += emojis.get(word, word) + ' '
# print(output)

# //////////////////////////////////////
#Functions


# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')


# print('Start')
# greet_user(last_name='Smith', first_name='John')


# def calc_cost(total, shipping, discount):
#     print(f'Hi {total} {shipping} {discount}!')


# calc_cost(total=50, shipping=20, discount=10)
# print('Finish')
# //////////////////////////////////////


# def square(number):
#     return number * number


# def square2(number):
#     print(number * number)
#     return None

# print('Result: ', square(30))
# //////////////////////////////////////

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ':)': '😊',
#         ':(': '😔',
#         ':D': '😃',
#         ':P': '😛',
#         '<3': '❤️'
#     }
#     output = ''
#     for word in words:
#         output += emojis.get(word, word) + ' '
#     return output


# message = input('> ')
# print(emoji_converter(message))

# //////////////////////////////////////
#Exceptions
# exit code 1 -> fail
# exit code 0 -> success


#HANDLE ERRORS
#Code no longer crush
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print(f'Invalid Value: {ValueError}')

# //////////////////////////////////////
#Classes
#Convention
#For clases dont use _, instead of this, use CapitalLetter to separate several words

# class Point:
#     def move(self):
#         print('move')

#     def draw(self):
#         print('draw')

# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 50
# print(point2.x)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print('move')

#     def draw(self):
#         print('draw')

# point = Point(10,20)
# point.x = 11
# print(point.x)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Hi I'm {self.name}")

# person = Person('John Smith')
# person.talk()
# # person.name = 'Fran'
# # print(person.name)

# bob = Person('Bob Smith')
# bob.talk()


# //////////////////////////////////////
#Classes Inheritance

# class Mammal:
#     def walk(self):
#         print('walk')


# class Dog (Mammal):
#     def bark(self):
#         print('bark')


# class Cat(Mammal):
#     pass


# dog1 = Dog()
# dog1.walk()
# dog1.bark()

# cat = Cat()
# cat.walk()

# //////////////////////////////////////
#Modules
# import converters
# from converters import kg_to_lbs

# print(kg_to_lbs(100))

# print(converters.kg_to_lbs(12))

# from utils import find_max

# find_max([1, 6, 45, 7, 88, 3])

# //////////////////////////////////////
#Packages
# import ecommerce.shipping
# from ecommerce import shipping
# from ecommerce.shipping import calc_shipping, calc_tax

# ecommerce.shipping.calc_shipping()
# shipping.calc_shipping()
# calc_shipping()
# calc_tax()

# //////////////////////////////////////
#Generating Random Values
# import random

# # for i in range(3):
# #     print(random.randint(10,20))

# members = ['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members)
# print(leader)


# class Dice:


#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         # return (first, second)
#         return first, second


# dice = Dice()
# print(dice.roll())

# //////////////////////////////////////
#Working with directories


from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# /usr/loocal/bin

# Relative path
# path = Path('ecommerce')
path = Path() #Current directory
# print(path.exists())
# print(path.mkdir())
# print(path.rmdir())
# print(path.glob('*')) FIND all files and directories
# print(path.glob('*.*')) all files
print(path.glob('*.py'))# all files .py
for file in path.glob('*.py'):
    print(file)

# //////////////////////////////////////
#Pypi AND Pip

# https://pypi.org/ 
#     Website with so many modules created by community
#         pokemon, openpyxl,...
#           pip3 install openpyxl
#https://www.yelp.es/madrid
#     Page to make scrapping


# //////////////////////////////////////
