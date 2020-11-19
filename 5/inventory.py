stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    total_items = 0
    print("Inventory:")
    for k, v in inventory.items():
        total_items += v
        print(str(v) + ' ' + k)
    print('Total number of items: ' + str(total_items))


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

displayInventory(stuff)
print(addToInventory(stuff, dragonLoot))
