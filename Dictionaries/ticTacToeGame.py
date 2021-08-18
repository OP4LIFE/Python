
# TIC-TAC-TOE GAME
print('\nTIC-TAC-TOE GAME')
print('Enter a number to draw the symbol on.\n')

# Modules.
import random

# Score counter.
score = {'X': 0, 'O': 0}

# A dictionary for storing moves.
board = {}

# Main loop.
while 1:
    board = {1: 1, 2: 2, 3: 3,
             4: 4, 5: 5, 6: 6,
             7: 7, 8: 8, 9: 9}
    
    # Function for cheking winning conditions.
    def conditions():
        conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], # Horizontal
                      [1, 4, 7], [2, 5, 6], [3, 6, 9], # Vertical
                      [1, 5, 9], [3, 5, 7]]            # Diagonal
        for condition in conditions:
            
            # If three in a row, announce it!
            if board[condition[0]] == board[condition[1]] == board[condition[2]] == ('X' or 'O'):
                return True
 
    # Game loop, player X starts.
    player = 'X'
    for move in range(9):
       
        # Printing the board.
        for key in range(1, 10):
            print(board[key], end = ' ')
            if key / 3 == int(key / 3):
                print()
        
        # Store the approproate symbol at the inputed number in the board dictionary.
        number = 
        while 1 <= number <= 9 and board[number] != 'X' or 'O':
        try:
        	number = int(input('\nPlayer ' + player + ': '))
        except:
        	number = int(input('\nPlayer ' + player + ': '))
 
        if 
            board[int(number)] = player
        else:
            board[int(input('\nPlayer ' + player + ': '))] = player
        
        #  Checking for three in row.  
        if conditions():
            score[player] += 1
            print('\n--------------------- \n' + \
                  'Player ' + player + ' is the winner \n\n' + \
                  'Player X wins: ' + str(score['X']) + '\n' + \
                  'Player O wins: ' + str(score['O']) + '\n' + \
                  '---------------------\n')
            break
        
        # Change players at the end of one's turn.
        if player == 'X':
        	player = 'O'
        else:
        	player = 'X'     	
       
       # Last move.
        if move == 8:
            print('It\'s a tie\n')
            break
        	   
    
