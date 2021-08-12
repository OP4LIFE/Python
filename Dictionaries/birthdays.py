print('BIRTHDAYS\n')

# Creating a dictionary where keys are names and values are dates.
birthdays = {'Matej': '23. January 2004'}

# Main program loop.
print('(i) In all cases, enter 0 or just enter to quit or cancel.\n')
name = 1 
while name:
    
    # Ask for a name and print the date.
    name = input('Name: ')
    if name in birthdays:
        print('Birthday: ' + birthdays[name] + '\n')
    
    # Otherwise, ask to add a date.
    elif name:
        date = input('Add a date: ')
        print()
        if date:
            birthdays[name] = date



