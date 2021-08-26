
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
   
# The function displays any inventory.
def display(inventory):
    print('\nInventory:')
      
    allItemsQuantity = 0
    for item, quantity in inventory.items():
        
        # Printing quantities and their associated items.
        print(quantity, item)
        
        # Counting a total number of items.
        allItemsQuantity += quantity

    print('Total number of items:', allItemsQuantity)

# The function adds items to the inventory.
def add(inventory, items):
    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    
    # Clear the items list.
    items = []


# Testing.
display(inventory)
print('\nAdding the loot to inventory...')
add(inventory, dragonLoot)
display(inventory)


