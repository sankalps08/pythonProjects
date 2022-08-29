from pprint import pprint

def find_next_empty(puzzle):
  #find the next row or col which is not filled yet represent it with -1
  #return row,col tuple(or(none,none) if ther eis none then show none )
  #keep in mind that we are using 0-8 indicies
  for r in range(9):
      for c in range(9):
          if puzzle[r][c] == -1:
            return r,c

  return None, None #if not space in puzzle are empty (-1)

def is_valid(puzzle, guess, row , col):
  #return true if it is valid other wise return false 
  #start with the row
  row_val = puzzle[row]
  if guess in row_val:
    return False


  #now col
  col_val = []
  for i in range(9):
    col_val.append(puzzle[i][col])
  if  guess in col_val:
    return False

  #now we have check square 
  #but we want to get where the 3*3 square starts and then we have to iterate over the 3 values in row/column

  row_start = (row // 3) * 3
  col_start = (col // 3) * 3

  for r in range(row_start, row_start + 3):
    for c in range(col_start, col_start + 3):
      if puzzle[r][c] == guess:
        return False

  #if we get here means all these return pass this and means that we get the value so we will return True here
  return True


def solve_sudoku(puzzle):
  #solve sudoku using backtracking
  #our puzzule is a list of lists, where each inner list is a row in our sudoku puzzle
  #return weather a solution exist
  #mutable puzzle to be the solution (If solution exists)

  #step -1 - choose somewhere on a puzzle to make a guess
  row, col = find_next_empty(puzzle)


  #if there is nowhere left then we are done because we only allow valid inputs
  if row is None:
    return True

  #step 2
  #if there is place to put a number then make a guess betwwen 1 and 9
  for guess in range(1,10):
    #step 3: checking weather the guess you have made is valid or not by checking the row and columns value return only if it is valid 
    if is_valid(puzzle, guess, row , col):
      #if our guess is valid then we will put our guess  into the puzzle
      puzzle[row][col] = guess
      #now we will recurse using this puzzle
      #step 4: recursively call our function
      if solve_sudoku(puzzle):
        return True

    #step- 5 what if it is not valid and sudoku puzzle is unsolvable because whatever we guessed did not work
    # then we have to backtrack and try a new number 

    puzzle[row][col] = -1 #reset the guess

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
  return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)