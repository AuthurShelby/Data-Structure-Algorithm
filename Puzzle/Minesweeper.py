import random 

# size is board size like eg :- 5x5
SIZE = int(input('Enter the size of the board you want :- '))
ROWS , COLS = SIZE , SIZE 

# setting the difficulty of the game.
# Accordint to difficulty the no.of mines vary.
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

  return board


