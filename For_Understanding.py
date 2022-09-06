import argparse
from functools import reduce
from logging import exception
from random import random
from tkinter import N
# this is just for understanding and for understanding basic feature and operations in python
# Asking user to enter first number then we will ask second number then we will sum first and second and get the addition
'''First_number = input("Enter the first number :")
Second_number = input("Enter the second number :")
Sum = float(First_number) + float(Second_number)

print("Sum :" + str(Sum)) 
'''

# this is to use if else conditions and check the weight in kg or lbs
#we will enter weight and then we will choose weather we want to see weight in kg or lbs or covert our own weight into kg or lbs

'''
Weight = int(input("Enter your weight:"))

Weight_unit = str(input("(K)g or (L)bs:"))

Kilo  = Weight/0.453592
lbs  = Weight*0.45
if Weight_unit.upper() == "K":
  print("Weight in lbs:" + str(Kilo))
elif Weight_unit.upper() == "L":
  print("Weight in kg:" + str(lbs))

'''

# Write Python3 code here

from email import parser
from unicodedata import name


class car():
	
	# init method or constructor
	def __init__(self, model, color):
		self.model = model
		self.color = color
		
	def show(self):
		print("Model is", self.model )
		print("color is", self.color )
		
# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()	 # same output as car.show(audi)
ferrari.show() # same output as car.show(ferrari)

# Behind the scene, in every instance method
# call, python sends the instances also with
# that method call like car.show(audi)


dog = {'name' : 'sankalp', 'age' : 23}
print(dog)

def greetings(name):
	print("hello, how are you doing " + name )

greetings("sankalp")
greetings("srishti")

items = [1,2,3,4]
items.append(5),items.append(6) 
print(items)

# classe and inheritance

class Animals:
	def walk(self):
		print("walking...")

class dog(Animals):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def category(self):
		print("My Dog is", self.name, "and he is ", self.age , "years old")

roger = dog("roger" , 8)
print("My Dog is", roger.name, "and he is ", roger.age , "years old")
roger.category()
roger.walk()


#lambda function
# lambda functions also called anynomous function , who don't have any name and only have one expression and that is the body 

lambda num: num*2

# they can be assigned 

multiply = lambda a,b : a * b
print(multiply(2,100))


#map(), filter() and reduce() - these are the global fucntions which can be used by collection  

numbers = [1,26,4,7,8,12]

result = map( lambda a: a*3 ,numbers) #map function #this will create a new list using your old list in map function we will pass function and the list name
print(list(result))


numbers1 = [1,2,4,6,8,1,4,23,54,65]

result1 = filter(lambda num: num % 2 == 0, numbers1) #filter() - this is filter function which we can use to filter from the list by using lambda function and giving some conditions
print(list(result1))
#accepting argument in codoe to work in command line 

#this is a list ofn  containing tuple
from functools import reduce	
listofnumdata = [   
	('hot', 80),
	('doc' ,21)
]

sum = reduce(lambda a,b: a[1] + b[1], listofnumdata)
print(sum)

#recursion --> the function which call itself is we called recursion
# for writing a recursive function we need to first write the base class function and other recursive function otherwise it will never stop and you will get recursive error,
#we will write factorial function

def factorial(n):
	if n == 1 : return 1
	return n*factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

#deceorators - enhance,alter and change the function how it works,decorators is defined by @symbol
# A decorator is a function that takes another function as a parameter  wraps a function in a inner function and perform the job it has to do  and return the inner function 
""" def logtime(func):
		def wrapper(val):
			print("hello top")
			val = func()
			print("hello bottom")
			return val
		return wrapper 

@logtime
def hello():
	print("hello middle")
hello() """  
# these 3 quotation in the start and the end we called them docstrings which will help you to understand about functions and methods and anythiong you write in code because when you will come after sometime you will not remember it or the code so this will explain you and the reader

#Annotation -  python is dynamically typed and in python we don't define the type of the variable but if you want to do it you can 

num: int =  4
print (num)
#and in function you can define as 
def number(n :int) -> int:
	return n
print(number(2))


# Exception ->> there is way to handle errors which python gives as a exception handling
# wrap your code arount the try block 

#try:
	#some code lines
#except<ERROR 1>: # except the errors that we will mention here 

#except<ERROR 1>: # the other error that can also happen 

#except: #these will except every error not any particular 

#else:
	#	no exception were raise the code ran successfully
#finally:
	# do something in any case , if no exception or anything done in code it will run no matter what 



try:
	result = 2/2
except ZeroDivisionError:
	print("you cannot divide by zero there should be number greater than zero")
finally:
	result = 1

print(result)

# you can alwayas use raise statment in you code by using raise menthod 

#raise Exception("An error!!") --> one way

try:
	raise Exception("An error!!")
except Exception as error:
	print(error)


#we can also pass exceptions in a class 
class DogNotFound(Exception):
		pass
try:
	raise DogNotFound
except DogNotFound:
	print("Dog is not found!	")

#with we can also use  in our code, in other words  is to be built in implicit exception handling as close file will be called automatically, this is only the one example of it 

""" filename = 'C:\Projects\python\Guess_game_user.py'
with open(filename, 'r') as file:
	content = file.read()
	print(content) """

# installing third part packages using pip

# pip install requests ( requests is a package )
#pip install -U requests (this is )


""" parser = argparse.ArgumentParser(
	description = 'this program print the name of my dog'
)

parser.add_argument('-c' ,  '--color' , choices = {"red ", "yellow"} , required = True, help = 'the color to search for ')

args = parser.parse_args()

print(args.color) """

#list compression --> it is a way to treat list in a very concise way
# list comprasion just m ake list and a code simpeler and short 


numbers = [1,2,3,4,5,6]
numbers_power2 = [n**2 for n in numbers]

print(numbers_power2)


#polymorphism --> polymorphism generalize functionality so it can work on different types 
# In this program we are assining some actions in eat function under dog and cat class
# then we wiss create objects for that class by assigining to some variable
#now we can call the function inside the class just by using . operator created object.function name 
import random
class dog:
	def eat(self):
		print("Dog is eating food")
		food_name = ['chinese' , 'south' , 'north']
		food_choice = random.choice(food_name)
		print('My dog is eating ' + food_choice)
class cat:
	def eat(self):
		print("cat is eating food")
		food_name1 = ['chinese' , 'south' , 'north']
		food_choice1 = random.choice(food_name1)
		print('My cat is eating ' + food_choice1)
	
animal_ch = dog()
animal_ch_2 = cat()

animal_ch.eat()
animal_ch_2.eat()


# Operator overloading 

class dog:
	def __init__(self, name ,age):
		self.name = name 
		self.age = age 
	def __gt__(self, other):
		return True if self.age > other.age else False

roger = dog('roger' , 9)
syd = dog('syd' , 7)

print (roger < syd)