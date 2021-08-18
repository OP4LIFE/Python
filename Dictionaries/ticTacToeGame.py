import random

# The code is for playing Tic-Tac-Toe
print('TIC-TAC-TOE GAME \n')
print('(i) Enter \'q\' to exit.')

board = {}
while 'q' not in board.values():
    # A dictionary for storing moves.
    board = {1: '_', 2: '_', 3: '_',
             4: ' ', 5: ' ', 6: ' ',
             7: '_', 8: '_', 9: '_'}
    
    # Function for cheking winning conditions.
    def conditions():
        conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], # Horizontal
                      [1, 4, 7], [2, 5, 6], [3, 6, 9], # Vertical
                      [1, 5, 9], [3, 5, 7]]            # Diagonal
        for condition in conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] == ('X' or 'O'):
                return 1
    
    # Random player start
    if random.randint(0, 1):
    	player = 'X'
    else:
    	player = 'O'
    
    # Player's turn
    def turn(player):
        board[int(input('Player X: '))] = 'X'
        
        # Printing the board.
        for i in range(9):
            print(list(board.values())[i])
            if i == 2 or 5 or 8:
                print()
        
        #  Checking for three in row.  
        if conditions():
            print('Player X is the winner')
            break
    
    # A loop for maximum of 9 moves for both players.
    # The starting player has 5 moves while the other has 4.
    for move in range(9):
    
        # Player X's turn
        board[int(input('Player X: '))] = 'X'
        # Printing the board.
        for i in range(9):
            print(list(board.values())[i])
            if i == 2 or 5 or 8:
                print()
        #  Checking for three in row.  
        if conditions():
            print('Player X is the winner')
            break
        # Last move.
        if i == 8:
            print('It\'s a tie')
            break
        
        # Player O's turn
        board[int(input('Player O'))] = 'O'
        # Printing the board.
        for i in range(9):
            print(list(board.values())[i])
            if i == 2 or 5 or 8:
                print()
        # Checking for three in row.
        if conditions():
            print('Player O is the winner')
            break
    
       
    