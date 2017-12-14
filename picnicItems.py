# Is testing the .center(), .rjust() and .ljust() functions.

def printDictionary(d, lWidth, rWidth):
    print('PICNIC ITEMS'.center(lWidth + rWidth, '-'))
    for k,v in d.items():
        print(("k is: " + k).center(lWidth + rWidth, ' '))
        print(("v is: " + str(v)).center(lWidth + rWidth, ' '))
        # Must cast v as string because value = int
    return 0

picnicItems = {'sandwiches':5, 'apples':3, 'bananas':7}

printDictionary(picnicItems, 20, 20)
