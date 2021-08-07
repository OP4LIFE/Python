# Coordinate field.
field = [ \
        [0, 0, 0, 0, 0, 0],  # y = 0
        [0, 0, 1, 0, 0, 0],  # y = 1
        [0, 0, 0, 1, 0, 0],  # y = 2
        [0, 1, 1, 1, 0, 0],  # y = 3
        [0, 0, 0, 0, 0, 0],  # y = 4
        [0, 0, 0, 0, 0, 0]]  # y = 5  
#   x =  0  1  2  3  4  5
# field[y][x]
for y in range(len(field)):  # E.g. field[0]
    for x in range(len(field[y])):  # E.g. field[0][0], field[0][1],...
        neighboursAlive = 0
        # Dead and live neighbours' coordinates based on the issued square - the missing field[y][x], which is not counted as a neighbour.

        # If the index is not 1, make it zero. IndexError: list index out of range
        corners = [x-1, x+1, y-1, y+1]
        for i in range(len(corners)):
            if corners[i] < 0 or corners[i] > len(corners)-1: # The second condition works only when x-axis and y-axis are the same lenght.
                corners[i] = 0
        left = corners[0]
        right = corners[1]
        top = corners[2]
        bottom = corners[3]
        allNeighbours = [ \
                         field[top][left],    field[top][x],    field[top][right],
                         field[y][left],                        field[y][right],
                         field[bottom][left], field[bottom][x], field[bottom][right]]
        liveNeighbours = 0
        for neighbour in allNeighbours:
            if neighbour:
                liveNeighbours += 1
        print('(' + str(x) + ', ' + str(y) + '): ' + str(field[y][x]) + ' with ' + str(liveNeighbours) + ' neighbours.')
        # E.g. '(3, 2): 1 with 3 neighbours.'
