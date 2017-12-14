#! python3

# Puropose: To back up a folder as a zip file, and each time it does so it
# makes a new numbered file and saves it to the cwd.

import zipfile, os

def zipBackup(folder):

    # Ensures that the folder's path is absolute and not relative.
    folder = os.path.abspath(folder)

    number = 1

    # Iterates through to the highest number of the file name in the cwd.
    while True:

        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'

        if not os.path.exists(zipFileName):
            break

        number += 1


    print("Creating %s..." % zipFileName)
    backupZip = zipfile.ZipFile(zipFileName, 'w')
    # nb: attribute is called ZipFile
    

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername) )
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # Continues the loop, doesn't back up the zip file

            backupZip.write( os.path.join(foldername, filename) )
    backupZip.close()
    print('Done.')


zipBackup('./cats')
