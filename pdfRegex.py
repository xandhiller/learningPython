import re

pdfRegex = re.compile(r'''
                        ^(\w+)
                        (.pdf)$
                        ''', re.VERBOSE)
