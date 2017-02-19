#fantasy game inventory
#displays inventory

fantasyInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    total = 0
    print("Inventory:")
    for k, v in inventory.items():
        total = total + v
        print(str(v) + " " + k)
    print("Total number of items: " + str(total))

displayInventory(fantasyInventory)
