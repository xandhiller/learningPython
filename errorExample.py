#! python3

# Purpose: To demonstrate traceback as a debugging technique.

def spam():
    bacon()

def bacon():
    raise Exception("This is the error message, yo'.")

spam()

# Traceback (most recent call last):
#   File "errorExample.py", line 11, in <module>
#     spam()
#   File "errorExample.py", line 6, in spam
#     bacon()
#   File "errorExample.py", line 9, in bacon
#     raise Exception("This is the error message, yo'.")
# Exception: This is the error message, yo'.

# The traceback allows you to go back to where the function was first called.
# The call stack shows you from top to bottom, oldest call, to most recent call.
# It details how the function was called, from the main section of the script
# all the way down to when the exception was called inside of the bacon function.
