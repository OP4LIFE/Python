

'''

CONWAYS GAME OF LIFE
Source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

The game is a cellular automaton devised by the British matehmatician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. 

Rules which shape the next generation:
1. rule: If a live square has two or three live neighbours, it stays alive, else it dies.
2. rule: If a dead square has exactly three neighbours, it becomes alive, else it stays dead.



NOTES FOR MODIFYING THE PROGRAM

Do not change the symbols for live and dead squares as it will interfere with the code.
The field should be a square (x and y-axis are the same length), otherwise the second condition on line 52 isn't correct.

'''

import copy 

# Creating a field of squares where each one has its own coorinates and a state. States of the dead squares are represented with zeroes, meanwhile states of the live squares are represented with ones. 
# Be aware that the square with coordinates (x, y) is obtained from the list with indexes field[y][x].
field = [[0, 0, 0, 0, 0, 0],  # y = 0
         [0, 0, 1, 0, 0, 0],  # y = 1
         [0, 0, 0, 1, 0, 0],  # y = 2
         [0, 1, 1, 1, 0, 0],  # y = 3
         [0, 0, 0, 0, 0, 0],  # y = 4
         [0, 0, 0, 0, 0, 0]]  # y = 5  
#    x =  0  1  2  3  4  5

# Creating a field where new states will be separately written so as to not influence the operating one.
nextField = copy.deepcopy(field)


# The main function which creates and prints the next generation based on the rules.
def generation():
    global field

    # The ensuing for loops allow us to read the squares' states.
    for y in range(len(field)):         # E.g. field[3]
        for x in range(len(field[y])):  # E.g. field[3][2]
           
            # Checking and fixing if neighbours' indexes are negative or out of list's range. May happen to squares at the edge of the field.
            checkIndexes = [x-1, x+1, y-1, y+1]
            for i in range(len(checkIndexes)):
                if checkIndexes[i] < 0 or checkIndexes[i] > len(field)-1:
                    checkIndexes[i] = 0

            # Creating a list of live and dead neighbours in order to count the live ones.
            left = checkIndexes[0]
            right = checkIndexes[1]
            top = checkIndexes[2]
            bottom = checkIndexes[3]
            allNeighbours = [field[top][left],    field[top][x],    field[top][right],
                             field[y][left],                        field[y][right],
                             field[bottom][left], field[bottom][x], field[bottom][right]]

            # Counting live neighbours.
            liveNeighbours = 0
            for neighbour in allNeighbours:
                if neighbour:
                    liveNeighbours += 1

            # 1. rule: If a live square has two or three live neighbours, it stays alive, else it dies. 
            if field[y][x]:
                if liveNeighbours == 2 or liveNeighbours == 3:
                    nextField[y][x] = field[y][x]
                else:
                    nextField[y][x] = 0
              
            # 2. rule: If a dead square has exactly three neighbours, it becomes alive, else it stays dead. 
            else:
                if liveNeighbours == 3:
                    nextField[y][x] = 1
                else:
                    nextField[y][x] = field[y][x]

    # Copying the modified field into the original one to provide new values for operation. Note that the list isn't copies just by reference.
    field = copy.deepcopy(nextField)
            
    # Print the generation.
    for line in nextField:
        print(line)        

# Interface.
print('\nCONWAYS GAME OF LIFE\nSource: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life\n')
print('Field: ')
for line in field:
    print(line)
print('\n\n')
print('Enter any key for next generation or \'q\' to quit.')
generations = [0]
for i in generations:
    if input() != 'q':
        print(str(i + 1) + '. generation')
        generation()
        generations += [generations[i] + 1] 
        
   

