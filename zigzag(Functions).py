# Settings
symbol_1 = ' '
symbol_2 = '*'
width = 15
start = 10
end = 15
step = 1

import time

end = end - 1
def image(start, end, step):
    for factor in range(start, end, step):
        print(symbol_1*factor + symbol_2*width)
        time.sleep(.1)
while 1:
	image(start, end, step)
	image(end, start, -step)

# It would be interesting to set the step variable to less than one, say .1, but that is not possible with range() function. We'll see what lists bring us in the next chapter. :D
