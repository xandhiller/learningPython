def collatz(number):
    try:
        if number % 2 == 0:
            print(number//2)
            return number//2
        if number % 2 == 1:
            print(number*3+1)
            return number*3+1
    except:
        print('Error.')

def runCollatz():

    print('Enter a number for the collatz function: ')

    while True:
        try:
            i = int(input())
            if i == 0:
                print('Entered zero, please don\'t.')
                continue
            break
        except:
            print('Invalid input. Please try again.')
            continue

    count = 0
    originalInput = i
    while i != 1:
        count = count+1
        i = collatz(i)

    print('\n\nThe number of iterations was: ' + str(count))

    if count == 0:
        print("The ratio is infinite, you likely entered one.")

    else:
        print('The ratio between iterations to input is: '+str(count/originalInput))

    print()


answer = None
while answer != 'n' and answer != 'N':
    runCollatz()
    print('Do you want to go again, y/n?')
    answer = str(input())
