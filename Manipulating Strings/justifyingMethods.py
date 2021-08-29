
# The following program simulates string methods for justifying text.
def rjust(width, string, fillchar = ' '):
    padding = (width - len(string)) * fillchar
    return padding + string

def ljust(width, string, fillchar = ' '):
    padding = (width - len(string)) * fillchar
    return string + padding

# center() Method.
def center(width, string, fillchar = ' '):
    if width < len(string):
        return string
    
    # reminder is due to even widths.
    padding = ((width - len(string)) // 2) * fillchar
    reminder = ((width - len(string)) % 2) * fillchar

    return padding + string + (reminder + padding)

# Testing.
# Lists of testing arguments.
widths = []
strings = ['', ' ', 'H', 'Hi', 'Hi!', 'Four']
fillchar = '*'

results = [[r'ljust()'], [r'rjust()'], [r'center()']]
for string in strings:
    
    # Creating a list of important widths.
    widths = []
    widths += [len(string) + 2, len(string) + 1, len(string), len(string) - 1, len(string) - 2, 0, -1, -2]
    
    for width in widths:
        results[0] += [ljust(width, string, fillchar) == string.ljust(width, fillchar)]
        results[1] += [rjust(width, string, fillchar) == string.rjust(width, fillchar)]
        results[2] += [center(width, string, fillchar) == string.center(width, fillchar)]

        # See where a method is malfunctioning.
#       if center(width, string, fillchar) != string.center(width, fillchar):
#           print(f'width {width}, string {string}, fillchar {fillchar}')
#           print(center(width, string, fillchar), string.center(width, fillchar), '', sep = '\n')

for method in [0, 1, 2]:
    if False in results[method]:
        print(results[method][0], 'method is malfunctioning.')
    else:
        print(results[method][0], 'method is confirmed.')

        
        
