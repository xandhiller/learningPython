theBoard = {'top-L': '   ', 'top-M': '   ', 'top-R': '   ',
            'mid-L': '   ', 'mid-M': '   ', 'mid-R': '   ',
            'low-L': '   ', 'low-M': '   ', 'low-R': '   '}

def printBoard():
    print("     |     |")
    print(" " + theBoard['top-L'] + " | " + theBoard['top-M'] + " | " + theBoard['top-R'])
    print("_____|_____|_____")
    print("     |     |")
    print(" " + theBoard['mid-L'] + " | " + theBoard['mid-M'] + " | " + theBoard['mid-R'])
    print("_____|_____|_____")
    print("     |     |")
    print(" " + theBoard['low-L'] + " | " + theBoard['low-M'] + " | " + theBoard['low-R'])
    print("     |     |")

def checkWin(x): # Player indicates 'O' or 'X'

    if theBoard['top-L'] == x: # checks top three and left three
        if theBoard['top-M'] == x and theBoard['top-R'] == x:
            return 1
        if theBoard['mid-L'] == x and theBoard['low-L'] == x:
            return 1

    if theBoard['low-R'] == x: # checks RHS vertical and bottom three
        if theBoard['mid-R'] == x and theBoard['top-R'] == x:
            return 1
        if theBoard['low-M'] == x and theBoard['low-L'] == x:
            return 1

    if theBoard['mid-M'] == x:
        if theBoard['top-L'] == x and theBoard['low-R'] == x: # diagonal
            return 1
        if theBoard['top-M'] == x and theBoard['low-M'] == x: # vertical middle
            return 1
        if theBoard['top-R'] == x and theBoard['low-L'] == x: # diagonal
            return 1
        if theBoard['mid-L'] == x and theBoard['mid-R'] == x: # horizontal middle
            return 1

    return 0


turn = ' X '
for i in range(9):
    printBoard()
    print("Turn for" + turn + ". Move on which space?")
    choice = input()
    theBoard[choice] = turn

    if checkWin(turn) == 1:  # checks if the current player won
        print("\n\n")
        printBoard()
        print("Player" + turn + "won.\n\n")
        break # exits program

    # Alternates turn.
    if turn == ' X ':
        turn = ' O '
    elif turn == ' O ':
        turn = ' X '
