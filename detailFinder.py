#! python

# Program purpose: To pull email addresses and phone numbers from text copied
# to the keyboard and display them to the user.

import re, pyperclip

# text = str('0412 345 678')    # Test string

text = str(pyperclip.paste())

# Mobile phone number regex

phoneRegex = re.compile(r'''
                        (\d{4}(\s)?)
                        (\d{3}(\s)?)
                        (\d{3})
                        ''', re.VERBOSE)

a = phoneRegex.findall(text)

# print(a)       # Testing


testE = 'fakeemail@gmail.com fakestudent@student.uts.edu.au'   # Test string

# TODO: Email regex
emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z]{2,4})
                        (\.[a-zA-Z]{2,4})?  # In case of ...(at)uts.edu.au
                        (\.[a-zA-Z]{2,4})?
                        (\.[a-zA-Z]{2,4})?
                        )''', re.VERBOSE)

# b = emailRegex.findall(testE)   # Testing email regex
# print(b)                        # Testing email regex


# TODO: Check through clipboard


# TODO: Display all results of the Check

# TODO: If no results, display nice message
