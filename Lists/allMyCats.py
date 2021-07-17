# Ask for the cat's name.
names = []
name = 1
while name != '':
    print('Enter either the name of the ' + str(len(names)+1) + '. cat or nothing to stop.')
    name = input()
    names = names + [name]
    
# Print all names. 
print('The cat names are:')
for name in names:
    print(name)
