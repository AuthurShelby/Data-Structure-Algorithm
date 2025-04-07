import random 
from collections import deque

# size is board size like eg :- 5x5
SIZE = int(input('Enter the size of the board you want :- '))
ROWS , COLS = SIZE , SIZE 

# for flood-fill algorithm 
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),         (0, 1),
              (1, -1), (1, 0), (1, 1)]

# setting the difficulty of the game.
# According to difficulty the no.of mines vary.
print('Enter the difficulty level you want:')
print(' 1) Easy\n 2) Medium\n 3) Hard')
difficulty = int(input('Choose (1/2/3): '))

while difficulty not in [1,2,3]:
  difficulty = int(input('Choose (1/2/3): '))

if difficulty == 1:
  mine_density = 0.10
elif difficulty == 3:
  mine_density = 0.20
else:
  mine_density = 0.15

# calculate the mines
MINES = int(ROWS*COLS*mine_density)

# printing info
print(f'Board Size - {SIZE}')
print(f'Game Difficulty - {difficulty}')
print(f'Mines set - {MINES}')

# creating the board
def create_board():
  
  # Initializing the board 
  board = [[' ' for i in range(COLS)] for i in range(ROWS)]
  # mines to store the position
  mines = set()
  
  # randomly placing the mines until the number of position is equal to MINES
  while len(mines) < MINES:

    row_index , col_index = random.randint(0,ROWS-1) , random.randint(0 , COLS-1)

    # if the (row,col) is not in the mines position
    # also this removes the entry of duplicate position
    if (row_index , col_index) not in mines: 

      mines.add((row_index , col_index))

      # making changes in the board
      # setting 'M' for mine
      board[row_index][col_index] = 'M'
    
    # setting the count of the mines for the neigbhouring cells 
    for row in range(ROWS):
      for col in range(COLS):
        if board[row][col] == 'M':
            continue
        counts = sum((row+dr , col+dc)in mines for dr , dc in DIRECTIONS) # check all the 8 direction of a cell
        board[row][col] = counts if counts > 0 else '.' # '.' are for the empty space

  return board

# flood-fill algorithm implemented using BFS 
# for revealing the cells 

# (0,0) — (0,1) — (0,2)
#  |       |       |
# (1,0) — (1,1) — (1,2)
#  |       |       |
# (2,0) — (2,1) — (2,2)

def reveal_empty_cell(board , visible , start_row , start_col):

  # if the starting cell is a number or a mine
  if board[start_row][start_col] !='.':
    visible[start_row][start_col] = True
    return 

  # intializing the queue with start_row & start_col
  queue = deque()
  queue.append((start_row , start_col))

  while queue:
    # poping out each of the cell row & col values to be revealed 
    row , col = queue.popleft()

    # checking boundries 
    if row < 0 or row >= ROWS or col < 0 or col >= COLS or visible[row][col]:
      continue
    
    # if it passes the conditon of boundries 
    visible[row][col] = True
    
    if board[row][col] == '.':
      # if it is empty then checks the neighboring cells
      for d_row , d_col in DIRECTIONS:
        new_row , new_col = d_row+row , d_col+col
        # again checks if it is not crossing the boundry 
        if 0 <= new_row < ROWS and 0 <= new_col < COLS and not visible[new_row][new_col]:
          queue.append((new_row , new_col))

# printing board
def print_board(board , visible):

    for row in range(ROWS):
      for col in range(COLS):
        print(board[row][col] if visible[row][col] else '■',end=' ')
      print()
    print()

def play_minesweeper():

  board = create_board()
  # cells that are visible to the player
  visible = [[False]*COLS for _ in range(ROWS)]
  while True:
    print_board(board , visible)
    # if the user gives without space
    print('\nRow and Column index starts from 0')
    row , col = (int(input('Enter the row value : ')) , int(input('Enter the column value : ')))
    
    if board[row][col] == 'M':
      print('Game Over! , You hit a mine.')
      break
  
    reveal_empty_cell(board , visible , row , col)

  # printing the whole after it exits the loop 
  print_board(board , [[True]*COLS for _ in range(ROWS)])

if __name__ == '__main__':
  # start the game
  play_minesweeper()
