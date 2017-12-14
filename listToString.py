def stringList(list1):

    leng = len(list1) # Get the length of list.

    for i in range(leng-1):
        print(str(list1[i]), end=' ', sep=', ')

    print("and " + str(list1[leng-1]), end='.\n')

# alex = ['alpha', 'bravo', 'charlie', 'delta']
# stringList(alex)

statement = [] # Essentially initialised the list. No elements in list.
while True:

# try:
    print(statement)
    print("Enter a list of items. When you're done, hit enter twice.")

    i = 0
    while True:
        i += 1
        element = str(input())  # Enter the string
        if element == '':       # Make sure they haven't just hit enter.
            break

        statement = statement + [element]  # Save the string to the list.

    if '' in statement:
        statement.remove('')    # Removes any spaces. 

    stringList(statement)
    break

    # except:
    #     print("Invalid input, please enter again.")
    #     continue
