import random

# The code is for playing Tic-Tac-Toe
print('TIC-TAC-TOE GAME \n')
print('(i) Enter \'q\' to exit.')

board = {}
while 'q' not in board.values():
    # A dictionary for storing moves.
    board = {1: '_', 2: '_', 3: '_',
             4: '_', 5: '_', 6: '_',
             7: '_', 8: '_', 9: '_'}
    
    # Function for cheking winning conditions.
    def conditions():
        conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], # Horizontal
                      [1, 4, 7], [2, 5, 6], [3, 6, 9], # Vertical
                      [1, 5, 9], [3, 5, 7]]            # Diagonal
        for condition in conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] == ('X' or 'O'):
                return 1
    
    # A loop for maximum of 9 moves for both players.
    # The starting player has 5 moves while the other has 4.
    player = 'X'
    for move in range(9):
        
        # Move stored in board dictipnary.
        board[int(input('Player ' + player + ': '))] = player
        
        # Printing the board.
        for key in range(1, 10):
            print(board[key], end = '')
            if key / 3 == int(key / 3):
                print()
        
        #  Checking for three in row.  
        if conditions():
            print('Player ' + player + ' is the winner')
            break
        
        # Change players at the end of the move.
        if player == 'X':
        	player = 'O'
        else:
        	player = 'X'     	
       
       # Last move.
        if move == 8:
            print('It\'s a tie')
            break
        	   
    
