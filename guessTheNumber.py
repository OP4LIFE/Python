# Izberi si številko med 1 in 20. Zapomni si jo. 
# Povej osebi: "I am thinking of a number between 1 and 20." 
# Vprašaj: "Take a guess." 
# Če je število manjše od prej izbranega, ugibajalcu namigni: "Your guess is too low. " in se ponovno vrni k vprašanju: "Take a guess." 
# Če je število večje od prej izbranega,  ugibajalcu namigni: "Your guess is to high. " in se ponovno vrni k vprašanju: "Take a guess." 
# Če je število enako prej izbranemu številu, ugibajalcu reči: "Good job! You guessed my number in [številka ugibov] guesses!"

import random
choosenNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
guessedNumber = ' '
numOfGuesses = 0
while choosenNumber != guessedNumber:
        numOfGuesses = numOfGuesses + 1
        print('Take a guess.')
        guessedNumber = input()
        if guessedNumber < choosenNumber:
                print('Your guess is too low.')
                continue
        elif guessedNumber > choosenNumber:
                print('Your guess is too high.')
                continue
print('Good job! You guessed my number in ' + numOfGuesses + ' guesses!')














