from organiserRegexes import pdfRegex, jpgRegex, pngRegex, pptRegex, wrdDocRegex,MatlabRegex
import os, shutil

def organiseDirectory(path):
    os.chdir('/')
    os.chdir(path)

    # Make the PDF folder to store all PDFs in.
    if not os.path.isdir('./PDFs'):
        os.mkdir('./PDFs')

    # Make the IMAGE folder to store all the images in.
    if not os.path.isdir('./Images'):
        os.mkdir('./Images')

    # Make the PowerPoint folder to store all the powerpoints in.
    if not os.path.isdir('./PowerPoints'):
        os.mkdir('./PowerPoints')

    # Make the WordDoc folder to store all the word documents in.
    if not os.path.isdir('./WordDocs'):
        os.mkdir('./WordDocs')

    # Make the WordDoc folder to store all the word documents in.
    if not os.path.isdir('./MATLAB'):
        os.mkdir('./MATLAB')

    # listdir() the directory and iterate through, moving PDFs into the folder.
    dirctry = os.listdir()

    # Moves PDFs to the 'PDFs' folder.
    for filename in dirctry:
        mo = pdfRegex.search(filename)

        if type(mo) == type(None):
            continue

        shutil.move('./'+ mo.group(), './PDFs')

    # Moves jpegs to the 'Images' folder
    for filename in dirctry:
        mo = jpgRegex.search(filename)

        if type(mo) == type(None):
            continue

        shutil.move('./'+ mo.group(), './Images')

    # Moves pngs to the 'Images' folder
    for filename in dirctry:
        mo = pngRegex.search(filename)

        if type(mo) == type(None):
            continue

        shutil.move('./'+ mo.group(), './Images')

    # Moves pptxs to the 'PowerPoints' folder
    for filename in dirctry:
        mo = pptRegex.search(filename)

        if type(mo) == type(None):
            continue

        shutil.move('./'+ mo.group(), './PowerPoints')


    for filename in dirctry:
        mo = wrdDocRegex.search(filename)

        if type(mo) == type(None):
            continue

        shutil.move('./'+ mo.group(), './WordDocs')

    for filename in dirctry:
        mo = MatlabRegex.search(filename)

        if type(mo) == type(None):
            continue

        shutil.move('./'+ mo.group(), './MATLAB')
