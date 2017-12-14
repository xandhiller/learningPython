name = input ('Enter your name: ' )
age = input('Enter your age: ')
age = int(age)
if name == 'Alice':
    print('Access granted')

if age<= 10:
    print("Woah, you're young!")
if age >= 21 + age < 65:
    print("Ah, an adult!")
if age > 65 + age < 127:
    print("Sure thing, granny.")
if age > 127:
    print("I'm skeptical.")
    
elif name != 'Alice' + name != '0':
    print('Access denied, please try again or enter 0 to exit.')
while name != 'Alice' + name != '0':
    name = input ('Enter your name: ' )
    age = input('Enter your age: ')
    age = int(age)

    if age<= 10:
        print("Woah, you're young!")
    if age >= 21 + age < 65:
        print("Ah, an adult!")
    if age > 65 + age < 127:
        print("Sure thing, granny.")
    if age > 127:
        print("I'm skeptical.")

    if name == 'Alice':
        print('Access granted')
    elif name == '0':
        break
    if name != 'Alice':
        print('Access denied, please try again')


