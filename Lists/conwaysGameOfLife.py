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
        left = x-1
        right = x+1
        top = y-1
        bottom = y+1
        # IndexError: list index out of range ,,, and negative indexes
# if any of them is negative, make it zero.
        if left < 0 or left > len(field[y])-1:
            left = 0
        if right < 0 or right > len(field[y])-1:
            right = 0
        if top < 0 or top > len(field)-1:
            top = 0
        if bottom < 0 or bottom > len(field)-1:
            bottom = 0
# if left < 0:
#    left = 0
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
