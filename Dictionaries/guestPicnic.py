
# The case-sensitive program operates with data inside a nested lists.
# The main list contains information about how many items will each person bring to a picnic.
allGuests = {'Alice': {'apples': 5, 'pretzels': 12}, 'Bob': {'ham sandwitches': 3, 'apples': 2}, 'Carol': {'cups': 3, 'apple pies': 1}}

# Creating a separate dictionary for summing up values of the same key.
itemsBrought = {}

# Iterate over the dictionaries containing all items and quantities of each person.
for allItems in allGuests.values():
  
  # Iterate over all individual items and quantities in the ongoing person's dictionary.
  for item, quantity in allItems.items():
  
    # If the item already exists in the "summing" dictionary, just add its quantity to the existing one,
    if item in itemsBrought.keys():
      itemsBrought[item] += quantity
    # otherwise, create an appropriate key-value pair in the "summing" dictionary.
    else:
      itemsBrought[item] = quantity

# Printing the "summing" dictionary.
print('Number of things being brought:')
for item, quantity in itemsBrought.items():
  print('-', item, quantity)  


