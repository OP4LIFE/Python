
# The program simulates the dictionary get() method using a normal function.

# Main function
def get(key, fallbackValue, dictionary):
    if key in dictionary.keys():
        return dictionary[key]
    else:
        return fallbackValue

# Testing
dictionary = {'key': 'key'}
print('Printing \'key\':', get('key', 'There is no such key', dictionary))
print('Printing \'There is no such key\':', get('Key', 'There is no such key', dictionary))



