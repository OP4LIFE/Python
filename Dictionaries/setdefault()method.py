
# The program simulates the dictionary setdefault() method using a normal function.

# The function
def setdefault(key, value, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        dictionary[key] = value
        return dictionary[key]

# Testing
dictionary = {'key': 'value'}

print('USING THE FUNCTION')
print('Printing \'value\':', setdefault('key', 'value', dictionary))
print('Printing \'new value\':', setdefault('key', 'new value', dictionary))
print('Printing the dictionary:', dictionary)
dictionary = {'key': 'value'}

print('\nUSING THE METHOD')
print('Printing \'value\':', dictionary.setdefault('key', 'value'))
print('Printing \'new value\':', dictionary.setdefault('key', 'new value'))
print('Printing the dictionary:', dictionary)


'''

Notice the behaviour where the keys where key passed to the method is the same, meanwhile the value is different.
In theory, the method should create two identical keys with seperate values.
What happens is, that the method prints 'New value' which isn't in any key-value pair.

'''


