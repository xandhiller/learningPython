#! python3

# Purpose: To trigger an assertion error if spam is less than 10.

import traceback    # traceback.format_exc()
import logging      # logging functions

logging.basicConfig(level = logging.DEBUG, format ='\
%(asctime)s - %(levelname)s - %(message)s' )
logging.disable(logging.CRITICAL) # Uncomment this to activate logging.


spam = input("Enter a value for spam: ")

logging.debug("Value of spam is: " + spam)

try:
    if int(spam) >= 10:
        print("Hooray! Spam is >= 10. :)")

except:
    errorFile = open("errorFile.txt", 'w')
    errorFile.write( traceback.format_exc() )
    assert int(spam) >= 10, "Spam is less than 10."
    errorFile.close()
