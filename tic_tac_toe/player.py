import math
import random

# This is a tic-tac-toe with various type of  player game where the 2 playes , 1 player vs computer and computer vs computer can play , player means human
# Here we will introduce classes where where we will split up out player and game in two classes , so we can actually play we can create the game and tell the game this is my X player and this is my O player


#Constructors are used to initializing the object’s state. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. 
#It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
#The keyword self represents the instance of a class and binds the attributes with the given arguments.
#Similarly, many objects of the Person class can be created by passing different names as arguments.
#self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
#The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes.
#we have used one class for player, this is our base class for player
#self.type_of_letter is gonna be X or O
#we want all players to get their next move  give a game
                                                      
#The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
 #this is for human player, this is our human player
 #The Python super() function returns objects represented in the parent’s class and enables multiple inheritances.
 #for human player moves , we wana thuman to choose the spot based on the input we provide to the computer
 #we want the  user to keep iterating until they achieve a valid square initially we will assign as false 
 #because user have not iput the value at this moment
 # We are going to check that this is the correct value by trying to cast
      # CASTING IN PYTHON- There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
      # It to an integer, if it's not then it's Invalid 
      # If the spot is avilable on the board we will say Not Empty 


#class RandomComputerPlayer(Player): #this class is used for computer player, this is our computer player
  #def __init__(self, type_of_player):
    #super().__init__(type_of_player) #The Python super() function returns objects represented in the parent’s class and enables multiple inheritances.

  #def get_move(self,game):
     #we use pass when we don't want to pass and arguments and condition and for future and don't need error if you don't use pass you will get error
     #square = random.choice(game.available_moves())

     #return square
     #get arandom valid spot for our next move

import math
import random
from turtle import position


class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


#here we will ise minisweep algorithm and after using this human will not be able to win this  game only computer will win that is it will become unbeatable game
# we will use minimax - that is decision making algorithm built on a maximizer and mini mizer concept
#we will use utility function 
class SmartRandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
      
    def get_move(self, game):
        if len(game.available_moves() ) == 9 :
            square = random.choice(game.available_moves())
        else:
          #we gonna use our minimize and maximize algorithm
          # #we gonna get the square based on our minimax algorithm 
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self,state, player):
        max_player = self.letter #yourself
        other_player = 'O' if player == 'X' else 'X' #other player
#we will check weather the previous move  WAS A WINNER OR NOT 
#this is our base case
        if state.current_winner == other_player:
          #we need to return score and position because we need to track  of the score 
          #for minimax to work
          #we are using the dictionary in this return statement
          #Dictionaries are used to store data values in key:value pairs.A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
          return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else 
                   -1 * (state.num_empty_squares() + 1)
               }
        elif not state.empty_squares():  #when no empty square left
          return {'position': None, 'score' : 0}

        if  player == max_player:
          best = {'position': None ,'score': -math.inf } #each score should be maximized (be larger)
        else:
          best = {'position': None ,'score': math.inf } #each score should be minimized (be smaller)

        for possible_moves in state.available_moves():
          #step -1 - make a move and try the spot 
          state.make_move(possible_moves, player)
          #step-2 - recurse using minimax to simulate a game after making that move 
          sim_score = self.minimax(state, other_player) #now , we alternate player 
          #step - 3 - undo the move 
          state.board[possible_moves] = ' '
          state.current_winner = None
          sim_score['position'] = possible_moves #otherwise this will get messed up from the recursion
          #step - 4 - update dictionaries if necessary
          if player == max_player:  #trying to maximize the max player 
            if sim_score['score'] > best['score']:
              best = sim_score  #replace best 
          else: # but minimize the other player 
            if sim_score['score'] < best['score']:
              best = sim_score #replace best 
        return best



