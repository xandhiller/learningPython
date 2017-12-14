from random import randint

n = int(randint(1, 10))

def guessCheck(guess):
    try:
        if n == guess:
            print('You got it!')
            return True
        if i == None:
            return False
        else:
            print ('Keep guessing.')
            return False
    except:
        print("Invalid input. Try again.")
        return False


print("I'm thinking of a number between 1 and 10 (inclusive).\n"
        "Guess what it is.")


i = None # Makes sure it's not a correct guess off the bat

while guessCheck(i) != True:
    try:
        i = int(input())
    except:
        print('Invalid input, please try again.')
    continue
