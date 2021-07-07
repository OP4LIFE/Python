# Settings
symbol_1 = ' '
symbol_2 = '*'
start = 0
width = 5
limit = 5
step = 1

multiply = 0
code = symbol_1*multiply + symbol_2*width
def right():
	for multiply in range(start, limit - 1, step):
		print(code)
def left():
	for multiply in range(limit - 1, start, -step):
		print(code)
while 1:
	right()
	left()
