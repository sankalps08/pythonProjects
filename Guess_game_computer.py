import random
""" def random_number(n):

  computer = random.randint(1,n)
  guess = 0
  while computer != guess:
    guess = int(input("Enter the number you want computer to guess: "))l
    if guess < computer:
      print("Too low ")
    elif guess > computer:
      print("Too High")
      break
    else:
      print("woohoo !! gotcha")  """
# We declare one function for writing code with computer guess name 
def computer_guess(x):
  # we provide low and high value so can computer generate numbers in between those value
  low = 1
  high = x
  guessed = ''   #this is used to tell computer weather his guess is low high or correct so he can generate random number above or below the number he just genrated
  while guessed != 'c':   #here we use while loop and check the the if the random number generated by computer is equal to guessed one or not
    if low != high:  #this is because what if the lowest and highest value is same or not 
      guess = random.randint(low,high)
    else: 
      guess = low #could be high as well because low is equal to high
    guessed = input(f"Is {guess} too high(H) or too low (L) or correct (C) ??").lower() #this is used to take input from user weather random number generated by computer is low high or correct by the user

    if guessed == 'h':
      high = guess - 1 #if the random number is high then it will -1 the number from the random number
    elif guessed == 'l':
      low = guess + 1 #if the random number is low then it will +1 the number from the random number

  print("woohoo !! computer guessed it right")  # this is used to print if you enter c that is when computer guessed the number you have in mind
computer_guess(100)  # this is used to assign high value by the user in which computer can generate numbers and  the closing argument of function

#random_number(10)
      
    






    