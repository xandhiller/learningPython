#! python
# makeDirectory.py - Creates a silly directory in the cwd.

import os, pprint, shutil

os.makedirs('''./blueberry/waffles/taste/great''')

# test = os.listdir('/')
# print("Output of os.listdir(): \n")

# pprint.pprint(str(test))

# for i in range(len(test)):
#     print(test[i])

input() # Allows me to pause and see if it worked.

for filename in os.listdir():
    if filename == 'blueberry':
        os.rmdir(os.getcwd() + '/blueberry/waffles/taste/great')
        os.rmdir(os.getcwd() + '/blueberry/waffles/taste')
        os.rmdir(os.getcwd() + '/blueberry/waffles')
        os.rmdir(os.getcwd() + '/blueberry')
