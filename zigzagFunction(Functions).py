import time
#start and end are the vertical lines, between which the pattern is limited.
def zigzag(start, end, width = 10, symbol = '*', step = 1, repeat = 10):
    for i in range(repeat):
        for factor in range(start, end - 1, step):
			print(' '*factor + symbol*width)
			time.sleep(.1)
		for factor in range(end - 1, start, -step):
			print(' '*factor + symbol*width)
			time.sleep(.1)
zigzag(0, 10)           
# It would be interesting to set the step variable to less than one, say .1, but that is not possible with range() function. We'll see what lists bring us in the next chapter. :D
# I will go to sleep normally no matter Python.
