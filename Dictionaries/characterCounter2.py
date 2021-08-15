
# The follow program prints the number of characters based on the text entered.
print('CHARACTER COUNTER 2')
print('(i) enter enter to exit.')

# Asks for text.
text = input('\nEnter text: ')

# Main loop.
characters = {}
for character in text:
    characters.setdefault(character, 0)
    character[character] += 1   

# Printing number of individual characters.
print('Characters: ')
for item in characters.items():
    print(item)



