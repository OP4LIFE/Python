
print('BIRTHDAYS Using Lists\n')

# Creating a list where each inner list contains a name and the associated birthday date.
birthdays = [['Matej', '23. January 2004'], ['Kiana', '24. March 2004']]

# Main program loop.
print('(i) In all cases, enter 0 or just enter to quit or cancel.\n')
name = 1 
while name:
    
    # Ask for a name and print the date.
    name = input('Name: ')
    for i in range(len(birthdays)):
        if name in birthdays[i]:
            print('Birthday: ' + birthdays[i][1] + '\n')
            break
  
        # Otherwise, ask to add a date.
        elif i == len(birthdays) - 1 and name:
            date = input('Add a date: ')
            print()
            if date:
                birthdays.append([name, date])

