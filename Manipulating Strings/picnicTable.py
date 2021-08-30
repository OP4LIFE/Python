
# The following program prints dictionary items in tabular view with correct spacing.

items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

def tabularPrint(dictionary, width):
    print('PICINC ITEMS'.center(width, '-'))
    for item, quantity in dictionary.items():
        print(item.ljust(width - len(str(quantity)), '.') + str(quantity))
        
tabularPrint(items, 17)

        
