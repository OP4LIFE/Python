
# The code is for playing Tic-Tac-Toe
print('TIC-TAC-TOE GAME \n')

# A dictionary which
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

# Winning conditions
def conditions():
    conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], # Horizontal
                  [1, 4, 7], [2, 5, 6], [3, 6, 9], # Vertical
                  [1, 5, 9], [3, 5, 7]]            # Diagonal
    for condition in conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == ('X' or 'O'):
            return 1

for i in range(8):

    # Player X's turn
    board[int(input('Player X: '))] = 'X'
    print(board)   
    if conditions():
        print('Player X is the winner')
        break
    if i == 7:
        print('It\'s a tie')
        break
    
    # Player O's turn
    board[int(input('Player O'))] = 'O'
    print(board) 
    if conditions():
        print('Player O is the winner')
        break

   
