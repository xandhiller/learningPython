import re

# Create regex to recognise PDFs
pdfRegex = re.compile(r'''
                        ^(.+)
                        (\.pdf)$
                        ''', re.VERBOSE)

# Create regex to recognise jpegs
jpgRegex = re.compile(r'''
                        ^(.+)
                        (\.jpg|\.JPG)$
                        ''', re.VERBOSE)

# Create regex to recognise pngs
pngRegex = re.compile(r'''
                        ^(.+)
                        (\.png|\.PNG)
                        ''', re.VERBOSE)

# Create regex to recognise pptxs
pptRegex = re.compile(r'''
                        ^(.+)
                        (\.pptx|\.PPTX)
                        ''', re.VERBOSE)

wrdDocRegex = re.compile(r'''
                            ^(.+)
                            (.+)?
                            (\.docx|\.DOCX|\.doc|\.DOC)
                            ''', re.VERBOSE)

MatlabRegex = re.compile(r'''
                            ^(.+)
                            (.+)?
                            (\.m|\.M|\.m~|\.M~)
                            ''', re.VERBOSE)
