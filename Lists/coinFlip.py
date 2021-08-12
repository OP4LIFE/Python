import random

# 100 times random flip
# check how many 6 same values in row
# repeat the process 10,000 times. 

values = []
sixInRow = 0
numOfFlips = 10000


for i in range(numOfFlips):
	values.append(random.randint(0, 1)) 

	# checking 6 in a row
for i in range(len(values) - 5):
	if values[i] == values[i + 1] == values[i + 2] == values[i + 3] == values[i + 4] == values[i + 5]:
		sixInRow += 1
	
# Print the possibility 
print('Coin flips:', numOfFlips)
print('Six same values in row:', sixInRow)
print('Possibility: %s%%' % ((sixInRow / numOfFlips) * 100))
