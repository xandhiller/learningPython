# import pprint

inventory = {'Arrow': 20, 'Gold coin': 21, 'Rope':10, 'Torch':1,
            'Dagger':1}

# pprint.pprint(inventory)

print() # Formatting

# print( str(inventory['Arrow']) + "\t" + "Arrow" + "hello", sep='x', end='\n')


for i in inventory:
    print( str(inventory[i]) + " " + i, sep='x', end='\n')

print() # Formatting
