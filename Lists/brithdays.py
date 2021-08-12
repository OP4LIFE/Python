
# Creating a dictionary where keys are names and values are dates.
birthdays = {'Matej': '23. January 2004'}

# Main program loop.
print('In all cases, enter 0 or just enter to quit or cancel.')
name = 1 
while name:
    
    # Ask for a name and print the date.
    name = input('Enter a name: ')
    if name in birthdays:
        print('Birthday date: ' + birthdays[name])
    
    # Otherwise, ask to add a date.
    elif name:
        date = input('Add a date: ')
        if date:
            birthdays[name] = date



