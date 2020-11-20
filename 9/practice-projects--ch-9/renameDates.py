#! /usr/bin/python3

# renames files with American dates to European dates

import shutil
import os
import re

datePattern = re.compile(r'''
   ^(.*?)            # text before date
   ((0|1)?\d)-       # one or two digits for month
   ((0|1|2|3)?\d)-   # one or two digits for day
   ((19|20)\d\d)     # four digits for year
   (.*?)$
''', re.VERBOSE)

# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# TODO: Skip files without a date.
    if mo == None:
        continue

# TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# TODO: Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + \
        monthPart + '-' + yearPart + afterPart

# TODO: Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

# TODO: Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
