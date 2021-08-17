
# The code is for playing Tic-Tac-Toe
print('TIC-TAC-TOE GAME \n')
print('(c) player vs computer \n (p) player vs player \n (cc) computer vs computer \n')
print('Which player do you want to be?')

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

# Winning conditions
def conditions():
    combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], # Horizontal
                    [1, 2, 7], [4, 5, 8], [7, 6, 9], # Vertical
                    [1 or 3 

    return \ # Horizontal        
        board[1] == board[2] == board[3] or \
        board[4] == board[5] == board[6] or \
        board[7] == board[8] == board[9] or \
          # Vertical
        board[1] == board[4] == board[7] or \
        board[2] == board[5] == board[6] or \
        board[7] == board[8] == board[9] or \
          # Diagonal
        board[1] == board[5] == board[9] or \
        board[3] == board[5] == board[9]

for i in range(8):

    # Player X's turn
    board[input('Player X: ')] = 'X'
    print(board)   
    if conditions():
        print('Player X is the winner')
        break
    if i == 7:
        print('It\'s a tie')
        break
    
    # Player O's turn
    board[input('Player O')] = 'O'
    print(board) 
    if conditions():
        print('Player O is the winner')
        break

   
