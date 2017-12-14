# Asks user to input all the names of their cats. Saves cats to a list.

print('Enter the names of all your cats.')
print('If you have entered all your cats, just press enter again.')

i = 0
catNames = []
while i != '':
    try:
        i = str(input())
    except:
        print('Invalid input.')
        continue

    catNames = catNames + [i]

catNames.remove('')

print('Number of cat names: ' + str(len(catNames)))
for i in range(len(catNames)):
    print(catNames[i])

print("Testing:")
print(catNames)
