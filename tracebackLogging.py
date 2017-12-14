#! python3

# Purpose: To demonstrate traceback logging.

import traceback

try:
    raise Exception("This is the error message.")
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback was written to errorInfo.txt')
