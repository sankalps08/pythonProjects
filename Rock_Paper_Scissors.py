import random 
# this random file we will use to generate random choice

def play():  #this function is use to show what is the conditiones required to play for user and computer
# here we will ask user to enter the input to know what he want to choose
  user = input("what is your choice ?? for rock press -(r),for paper press -(p) , for scissors press -(s)")

  computer = random.choice(['r','s','p']) # these 3 options are the computer choice where it will use any one of em randomly

  if user == computer:  #here if the choice of user and the computer match it will consider to be a tie
    return 'It\'s a Tie'  

# r>s , p>r , s>p 
  if is_win(user,computer):
    return "You Won"  # here we are comparing value of user and computer by using is_win function and if condition match it will win otherwise it will show loose
  return "You Lost!!"

def is_win(player,opponent):  #here we are creating one function to see in which case one person win
   #return true if the player wins
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'): 
    return True
    # in this we are checking all the conditions where and comparing it with the user and opponent choice if the choicses
    # come in the if case and player will choose rock and computer s then user will win
print(play())


# we can also loop this game and give user three live like best of 3 and then give total number of wins to either user or computer