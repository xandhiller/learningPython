def addToInventory(playerInv, loot):
    for i in loot:
        # print(i)
        playerInv.setdefault(i, 0)
        playerInv[i] += 1

    # print(playerInv)
    # No need to return playerInv, as the inventory dictionary was
    # passed by reference. So when it is edited here, it is edited
    # globally. At least, that's what I think, anyway.

def displayInventory(playerInv):
    print("\nAfter:")

    count = 0
    # You have to include this as an initial assignment for the loop
    # to work. 

    for i in playerInv:
        print(str(playerInv[i]) + " " + i)
        count += playerInv[i]
    print("Total number of items: " + str(count))
    print()

inv = {'gold coin': 42, 'rope': 1}
print("\nBefore:")
print(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)

# inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
