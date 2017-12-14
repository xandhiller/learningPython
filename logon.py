password = '' #initialise the variable so python
while password != 'get schwifty':
    print('Enter Username: ')
    name = input()

    if name == 'Gazorpazorp':
        print ('Enter password: ')
        password = input()
        continue
        if password == 'get schwifty':
            print('Access granted.')
        if password != 'get schwifty':
            continue

    else:
        print('Wrong username.')
