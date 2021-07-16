# A list of pets.
pets = ['Blacky', 'Bobby']
pet = 1

# Ask for a guess.
print('Press enter to quit.')
print('Guess what\'s the name of my pet.')
while pet != '':  
    pet = input()
    # Check the guess.
    if pet in pets:
        print('You guessed!')
        break
    elif pet != '':
        print('Try again!')