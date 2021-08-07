# If list's axis are not the same length, the second condition on line 22 will be amiss.
# Note that the condition on line 38 works only if live states are not labeled with falsey values ('', 0, 0.0).

# Creating a field of squares where each one has its own coorinates and a state. States of the dead squares are represented with zeroes, meanwhile states of the live squares are represented with ones. 
# Be aware that the state of a field with coordinates (x, y) is obtained from the list with reversed indexes field[y][x].
field = [[0, 0, 0, 0, 0, 0],  # y = 0
         [0, 0, 1, 0, 0, 0],  # y = 1
         [0, 0, 0, 1, 0, 0],  # y = 2
         [0, 1, 1, 1, 0, 0],  # y = 3
         [0, 0, 0, 0, 0, 0],  # y = 4
         [0, 0, 0, 0, 0, 0]]  # y = 5  
#    x =  0  1  2  3  4  5

# The ensuing for loops allow us to read the fields' states.
for y in range(len(field)):         # E.g. field[3]
    for x in range(len(field[y])):  # E.g. field[3][2]
        # Dead and live neighbours' coordinates based on the issued square - the missing field[y][x], which is not counted as a neighbour.

        # Checking and fixing if neighbours' indexes are negative or out of list's range. May happen to squares at the edge of the field.
        checkIndexes = [x-1, x+1, y-1, y+1]
        for i in range(len(checkIndexes)):
            if checkIndexes[i] < 0 or checkIndexes[i] > len(checkIndexes)-1: # The second condition works only when x-axis and y-axis are the same lenght.
                checkIndexes[i] = 0

        # Creating a list of live and dead neighbours.
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
        print('(' + str(x) + ', ' + str(y) + '): ' + str(field[y][x]) + ' with ' + str(liveNeighbours) + ' neighbours.')
        # E.g. '(3, 2): 1 with 3 neighbours.'

        # Changing the items in the field based on rules.

        


















