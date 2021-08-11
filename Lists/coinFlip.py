import random

# 100 times random flip
# check how many 6 same values in row
# repeat the process 10,000 times. 

sixInRow = 0 

for i in range(10000):
	
	# 100 random flips stored
	flips = []
	for i in range(100):
		flips.append(random.randint(0, 1)) 

	# checking 6 in a row
	for i in range(len(flips) - 5):
		if flips[i] == flips[i + 1] == flips[i + 2] == flips[i + 3] == flips[i + 4] == flips[i + 5]:
			sixInRow += 1
	
# Print the possibility 
print('Coin flips: 10.000 * 100')
print('Six same values in row: ' +str(sixInRow))
print('Possibility ', 100 * sixInRow // 1000000, '%', sep = '')
