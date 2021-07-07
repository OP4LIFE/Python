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
