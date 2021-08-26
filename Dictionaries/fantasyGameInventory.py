
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
secondInventory = {'rope': 3, 'torch': 2, 'gold coin': 23}
   
# The function displays any inventory.
def displayInventory(inventory):
    print('\nInventory:')

    allItemsQuantity = 0
    for item, quantity in inventory.items():
        
        # Printing quantities and their associated items.
        print(quantity, item)
        
        # Counting a total number of items.
        allItemsQuantity += quantity

    print('Total number of items:', allItemsQuantity)

# Testing displayInventory().
displayInventory(inventory)
displayInventory(secondInventory)


