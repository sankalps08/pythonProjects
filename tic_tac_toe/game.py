import math
import time
from player import HumanPlayer, RandomComputerPlayer,SmartRandomComputerPlayer # we are importing players function in this and their operations



#we will ujse current winner as none in start
#this fucntion will be using to design 3*3 board we created spaces for 9 numbers so using this fuction we will divide the line into rows and create a 3*3 matrix
#as you can see we are using the for loop for dividing self.board 9 line into 3 each for 3*3 matrix by giving range 3, when i will be 0 loop will continue  till 0,1,2  then it will go in next row and print | for 3,4,5
#print(' __ ' + ' __ '.join(row) + ' __ ')
# this is a static method in python that is, it is related to class of tic tac toe not to the objects of that class, and this will not be related or affect init functions
#this function is used to right numbers in the boxes so can player choose betwwen those numbers and choose where they wanna use their chance 
#str is used because we can print string and I will be in integer so for printing purpose we used this
#print(' __ ' + ' __ '.join(row) + ' __ ')
 # Now we right Logic of the game
# return true if valid otherwise return false
#if valid move, make a move and assign square to type_of_player
#winner if 3 in a row anywhere, we have to check row , colum and diagonal to meet the winner condition
#there would be 3 case where player can win , when it will get 3 in a row,coulumnm and diognal in the game 
    #let's check the row
#now we will check the case of diagonal, only way to win a diagonal is to only when square is 0,2,4,6,8
#in this we will return list and know where we can use our player to put X or O

#tHIS IS THE METHOD WE call list comprehension #List comprehensions provide a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
""" moves = []  # ENUMERATE -- If we want to convert the list into an iterable list of tuples (or get the index based on a condition check, for example in linear search you might need to save the index of minimum element), you can use the enumerate() function. 
    for (i,spot) in enumerate(self.board):
      #['x' , 'x' , 'o']  --> [(0,'x'), (1,'x'), (2,'o')]
      if spot == ' ':
        moves.append(i)
    return moves """

#we gonna return the winner with name of player and None for a tie
# Starting letter 
    # iterate while the   game still have empty square
    # WE DON'T HAVE TO WORRY ABOUT WINNER because we will just return that which breaks the loop
#lets define a function to actually make a move
 #after we made our move we need to alternate the move

#I'm going to use time.sleep just to give a littile pause in each iteration

""" if letter == 'X':
        letter = 'O'
      else:
        letter = 'X' """


import math
import time
from player import HumanPlayer, RandomComputerPlayer

# this is the main class of the game under this we will print board first
class TicTacToe():
    def __init__(self): ##this is a constructor for creating the board
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]  ##we will use a single list to rep 3*3 board

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('_|_' + '__|_'.join(row) + '_|_')
            print(' | ' + '   | ' + '   | ' + '  |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('_|_' + '__|_'.join(row) + '_|_')
            print(' | ' + '   | ' + '   | ' + '  |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'O'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


#__name__ == ‘__main__’ is used in a Python program to execute the code inside the if statement only when the program is executed directly by the Python interpreter. When the code in the file is imported as a module the code inside the if statement is not executed.

if __name__ == '__main__':
    x_player = SmartRandomComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)