
# The following program counts the occurrences of characters in text entered.
print('CHARACTER COUNTER')
print('The counter is case-sensitive.')
print('(i) Enter enter to exit.')
string = 1
while string:
	
	# Ask for a string.
	string = input('\nEnter some text: ')
	
	# A dictionary for storing 	occurrences.
	occurrences = {}
	
	# A loop for storing occurances.
	for i in range(len(string)):
	
	    # If the character is already in occurrences dictionary, add one,    
	    if string[i] in occurrences.keys():
	        occurrences[string[i]] += 1
	    # else, create a key for the character and set its value to one for the first occurrence.
	    else:
	        occurrences [string[i]] = 1
	
	# Printing occurrences
	print('Occurrences: ')
	for item in occurrences.items():
	    print(item)


