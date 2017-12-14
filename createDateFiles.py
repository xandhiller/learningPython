#! python3

# Purpose: To create files in the cwd in order to test convDatesAmerToEur.py

import shutil, os

def createAmerFiles():
    month = 1
    day = 10
    year = 2005

    for i in range(5):
        f = open('%.2d-%.2d-%.4d.txt' % (month, day, year),'w', )
        f.write('blah blah this is %2.d-%2.d-%4.d' % (month, day, year) )
        f.close()
        month += 1
        day += 1
        year += 1
