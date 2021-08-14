
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
print(setdefault('key', 'value', dictionary)


