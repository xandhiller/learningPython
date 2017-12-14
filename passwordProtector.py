#! python
# password protector

import pyperclip

passwords = {'gmail':'password','Phone':'123456','luggage':'1234',
            'reddit':'aXeTyJhKls12304858'}



while True:
    print("\n\nPlease enter the account's password you would  ", end ='')
    print("like copied to the clipboard. \nEnter 'E' to exit.")

    account = input()

    if account == 'E':              # Condition to exit program.
        print('\n'*2)
        print("Program exitting.")
        print('\n'*2)
        break                       # Exits

    p = passwords.get(account, 0)   # Checks if password for thing is in
                                    # database else returns 0
    if p == 0:
        print('\n'*2)
        print("Password for " + account + " is not in the database.")
        print('\n'*2)
        continue                    # Returns to beginning.


    else:
        pyperclip.copy(p)           # Copies password to clipboard.
        print('\n'*2)
        print("Successfully copied password to clipboard.")
        print('\n'*2)
