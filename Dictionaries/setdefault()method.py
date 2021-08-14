
# The program simulates the dictionary setdefault() method using a normal function.

# The function
def getdefault(key, value, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        dictionary[key] = value
        return dictionary[key]

# Testing
dictionary = {
