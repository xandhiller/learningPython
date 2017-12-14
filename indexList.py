from random import randint

print("Enter values into the list. When you're done just press enter again.")

list = ['']
list[0] = str(input())

i = None
while i != '':
    try:
        i = str(input())
        list = list + [i]
    except:
        print('Invalid input.')

# Even if there is multiple spaces, they will all be removed.
list.remove('')

# Saves the initial value of the list.
# That way it can be indexed easier later.
initialCount = len(list)
print("Length is: " + str(initialCount))

# Produces random number to randomly select an index
# Adds randomly selected indexes contents to the list again
# This duplicates the items in the list
for i in range(20):
    n = randint(0, len(list)-1)
    list.append(str(list[n]))




print("List is:")
print(list)
print()


# Indexing the list
#for i in range(0, initialCount):
#    print("List element " + str(i) + " is: " + list[i])
#    print("This occurs " + str( list.index(list[i]) ) + " times.\n\n")

# Indexing returns the element number of the array that the entered
# string is present in.
# I originally thought it told you how many times it was in the list. 
