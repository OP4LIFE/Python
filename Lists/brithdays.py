'''

The following program prints the birthday date associated with the entered name.
If the name doesn't exists, the program will ask you to add one.
In all cases, you enter 0 or just enter to quit or cancel.

'''

# Creating a dictionary where keys are names and values are dates.
birthdays = {'Matej': '23. January 2004'}

# Main program loop.
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
