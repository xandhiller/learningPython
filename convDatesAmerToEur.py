#! python3

# Purpose: Converts the dates of .txt files in the directory from an
# american format to a european format.

import os, re, sys, createDateFiles, shutil

# TODO: Make a regex to identify dates

# TODO: Use regex to work through the os.listdir(), selecting those that fit
# and then rename the file with shutil.move()

amerDateRegex = re.compile(r'''
                            (.*)?                      # Possible word
                            (\d{2})-(\d{2})-(\d{4})    # Date
                            (.*)?                      # Possible word
                            (.txt)$                    # File must end in '.txt'
                            ''', re.VERBOSE)

# Stores all the files and folders in the cwd in a list called directory.
directory = os.listdir( os.getcwd() )

# Find all files to be renamed and store in mustRename
mustRename = list( filter(amerDateRegex.match, directory) )



for filename in mustRename:
    mo = amerDateRegex.search(filename)

    newFileNameAndPath = os.getcwd() + '/' + \
                        str( nmo.groups(1) ) + str( nmo.groups(3) ) + str( nmo.groups(2) ) + str( nmo.groups(4) ) + str( nmo.groups(5) ) + str( nmo.groups(6) )
    newFileNameAndPath.replace(" ", "")

    shutil.move( os.getcwd() + filename,  newFileNameAndPath)
