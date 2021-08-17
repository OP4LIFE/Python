
# The code is for playing Tic-Tac-Toe
print('TIC-TAC-TOE GAME \n')
print('(c) player vs computer \n (p) player vs player \n (cc) computer vs computer \n')
print('Which player do you want to be?')

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

# Rules
rules = \ # Horizontal
        board[1] == board[2] == board[3] or \
        board[4] == board[5] == board[6] or \
        board[7] == board[8] == board[9] or \
          # Vertical

        board[1] == board[4] == board[7] or \
        board[2] == board[5] == board[6] or \
        board[7] == board[8] == board[9] or \

          # Poeševno
        board[1] == board[5] == board[9] or \
        board[3] == board[5] == board[9] or \





for i in range(8):
    board[input('Player X:')] = 'X'
    print(board)
    
    if rules:
        print('Player X is the winner')
        break
    elif i == 7:
        print('It\'s a tie')
        break
    
    
    board[input('Player O')] = 'O'
    print(board)
    
    if rules:
        print('Player O is the winner')
        break
    # Not protecteed
    # Check the references for ru!es, if everything worjs out.
    # Gotta make a razumen loop for an interface.
