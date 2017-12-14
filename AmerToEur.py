#! python3

# Purpose: To convert the files in the cwd form american dates to european.

import shutil, os, re

datePattern = re.compile(r'''
                        ^(.*?)              # Text before date
                        ((0|1)?\d)-         # Month
                        ((0|1|2|3)?\d)-     # Day
                        ((19|20)\d\d)       # Year
                        (.*?)$              # Word after or file extension
                        ''', re.X)

for amerFileName in os.listdir('.'):

    mo = datePattern.search(amerFileName)

    if mo == None:
        continue

    prologue = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    epilogue = mo.group(8)

    eurFileName = prologue + day + '-' + month + '-' + year + epilogue

    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    eurFileName = os.path.join(absWorkingDir, eurFileName)

    # Rename files:
    print("Renaming %s to %s" % (amerFileName, eurFileName))
    shutil.move(amerFileName, eurFileName) # Uncomment after testing.
