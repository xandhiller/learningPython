#! python3

# Purpose: To demonstrate the use of the logging module.

import logging

logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s \
- %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # Uncomment this to activate logging. 

logging.debug('Start of program.')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % str(n) )
    total = 1
    for i in range(1, int(n)+1, 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total) )
    logging.debug('End of factorial(%s%%)' % str(n) )
    return total

n = input("Enter a number to take the factorial of: ")
print( str(factorial(n)) )
logging.debug("End of program.")
