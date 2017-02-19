#fantasy game inventory
#adds loot to inventory and displays it



dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}


#setdefault method assigns new loot value as 0
#next step- increases the count by 1 for already existing loot; sets 1 for new loot

def addToInventory(inventory, loot):
    for item in loot:
        inventory.setdefault(item,0)
        inventory[item]+= 1


def displayInventory(inventory):
    total = 0
    print("Inventory:")
    for k, v in inventory.items():
        total = total + v
        print(str(v) + " " + k)
    print("Total number of items: " + str(total))

addToInventory(inv, dragonLoot)

displayInventory(inv)
