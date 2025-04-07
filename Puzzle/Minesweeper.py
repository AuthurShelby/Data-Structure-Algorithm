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
MINE = int(ROWS*COLS*mine_density)
