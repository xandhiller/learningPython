elements = 4    # Number of elements per nested list.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

n = 0 # Initialise the counter



# Find the max string length
maxLength = 0

for i in range(elements):

    for j in range(len(tableData)):
        if maxLength < len(tableData[j][i]):
            maxLength = len(tableData[j][i])   # Set max length to biggest size

# print("Max length is: " + str(maxLength))



for i in range(elements): # for i in range of number of elements in a list

    for j in range(len(tableData)): # For j in range of number of lists

        print(tableData[j][i].rjust(maxLength), end='')
        n += 1

        if n == 3:  # Number of columns printed
            n = 0
            print()
