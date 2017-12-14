#! python3

# Purpose: To detect if two strings are the same, despite case.

import logging

logging.basicConfig(filename = 'loggingData.txt', level=logging.DEBUG, format ='\
%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # Uncomment this to activate logging.


first = input("Enter the first string: ")
second = input("Enter the second string: ")

logging.debug("First string: %s" %first.lower() )
logging.debug("Second string: %s" %second.lower() )

if first.lower() == second.lower():
    print("They match! (This is not case sensitive).")
else:
    print("The strings do not match.")
