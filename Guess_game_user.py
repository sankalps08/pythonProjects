import random
# this randam file is to use random words,charachter and integer etcc. This is the package come with python and there are so many 
# function accessible to you just by importing this random 

# In this programm we will guess the random number genrated by the computer random function

# first we need to define one function, and for defining function in python we usee def
# we have defined the function name guessed number and passed the n as a parameter of thta function
def guessed_number(n):
# this random.randint is a inbuilt function in python for generating random number that is why we import random to access this function
# we will store the random number genrated by the computer in random_number variable
  random_number = random.randint(1,n)  
  #guessed number is that number we enter or guess
  # first step is that we will start while loop and that loop will go on till we not guess  the random number genrated by computer
  guessed_number = 0
  while guessed_number != random_number:
    guessed_number = int(input(f"Guess a numbeer betwwen 1 and {n}: "))    # ask user to guess the number
    if guessed_number < random_number: #if the guess number is low then random number then we will print too low se we can guess another number greater than that
      print("Too low")
    elif guessed_number > random_number:
      print("Too High")
  
  print(f"woohoo! You guessed the right number that is {random_number}")  #if we guessed the same number it will show this message 


guessed_number(20)

#in the end we pass the value in the guessed function