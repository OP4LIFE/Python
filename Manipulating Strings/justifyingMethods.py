
# The following program simulates string methods for justifying text.

# rjust() Method.
def rjust(width, string, fillchar = ' '):
    padding = (width - len(string)) * fillchar
    return padding + string

print('\nTesting rjust():')
print(rjust(6, 'Hi', '*'), 'Hi'.rjust(6, '*'))
print(rjust(5, 'Hi', '*'), 'Hi'.rjust(5, '*'))
print(rjust(2, 'Hi', '*'), 'Hi'.rjust(2, '*'))
print(rjust(1, 'Hi', '*'), 'Hi'.rjust(1, '*'))
print(rjust(-1, 'Hi', '*'), 'Hi'.rjust(-1, '*'))

# center() Method.
def center(width, string, fillchar = ' '):
    if width < len(string):
        return string
    
    # reminder is due to even widths.
    padding = ((width - len(string)) // 2) * fillchar
    reminder = ((width - len(string)) % 2) * fillchar

    return (reminder + padding) + string + padding

# rleft, testing loop      

print('\nTesting center():')
print(center(6, 'Hi', '*'), 'Hi'.center(6, '*'))
print(center(5, 'Hi', '*'), 'Hi'.center(5, '*'))
print(center(2, 'Hi', '*'), 'Hi'.center(2, '*'))
print(center(1, 'Hi', '*'), 'Hi'.center(1, '*'))
print(center(-1, 'Hi', '*'), 'Hi'.center(-1, '*')) 


