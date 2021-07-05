import random, sys
print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0
choosenMove = ''
while choosenMove != 'q':
	print('{} wins, {} losses, {} ties'.format(wins, losses, ties))
	print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit.')
	# Player choosing
	choosenMove = input()
	if choosenMove == 'r':
		print('ROCK versus...')
	elif choosenMove == 'p':
		print('PAPER versus...')
	elif choosenMove == 's':
		print('SCISSORS versus...')
	else:
		continue
	# Computer choosing
	oppositeMove = random.randint(1, 3)
	if oppositeMove == 1:
		oppositeMove = 'r'
		print('ROCK')
	elif oppositeMove == 2:
		oppositeMove = 'p'
		print('PAPER')
	else:
		oppositeMove = 's'
		print('SCISSORS')
	# Rules of the game are what follows
	'''
	r r	(tie)	p r (win)	s r (lose)
	r p	(lose)	p p (tie)	s p (win)
	r s (win)	p s (lose)	s s (tie)
	'''
	cM = choosenMove
	oM = oppositeMove
	if cM == oM:
		print('It is a tie!')
		ties = ties + 1
	elif (cM == 'r' and oM == 'p') or (cM == 'p' and oM == 's') or (cM == 's' and oM == 'r'):
		print('You lose.')
		losses = losses + 1
	else:
		print('You win.')
		wins = wins + 1
sys.exit()
		
	
	
