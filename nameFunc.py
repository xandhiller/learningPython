import random

def ola(name):
    print('Ola!')
    print('Your name is ' + name)
    print('I know that\'s a bit creepy, sorry.')

def platitude(randInt):
    if randInt == 1:
        return 'Yeah, I don\'t know about that.'
    elif randInt == 2:
        return 'It\'s possible, but only if you put your mind to it.'
    elif randInt == 3:
        return 'Life\'s hard. You may not achieve that now, but maybe one day.'
    elif randInt == 4:
        return 'I know that if you try really hard, you can achieve anything.'
    elif randInt == 5:
        return 'Only you can determine whether or not you are able to do that.'
    elif randInt == 6:
        return 'That\'s totally doable! You\'ve got this!'

while 1>0:
    print('\nThis program aims to provide you with expert life advice. \n')
    print('Think really hard about what it is you want to achieve. Then press enter.')

    input()
    n = random.randint(1,6)
    advice = platitude(n)
    print(advice)
