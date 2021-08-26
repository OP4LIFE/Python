
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# The function sorts an inventory by keys.


# The function displays any inventory.
def displayInventory(inventory):
    print('Inventory:')
    
    # Sorting the inventory alphabetically.
    inventory.sort()

    allItemsQuantity = 0
    for item, quantity in inventory.items():
        # Printing items and their quantity.
        print(quantity, item)
        
        # Counting a total number of items.
        allItemsQuantity += quantity

    print('Total number of items:', allItemsQuantity)

# Testing displayInventory().
displayInventory(inventory)
