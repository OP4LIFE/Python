names = []
name = 1
while name != '':   # Ask for a name.
    print('Enter either the name of the ' + str(len(names)+1) + '. cat or nothing to stop.')
    name = input()
    names = names + [name]
print('The cat names are:')     # After stopping, print all names. 
for index in range(len(names)):
    print(names[index])
