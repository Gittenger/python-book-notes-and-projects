#! /usr/bin/python3

# copies a folder and its contents into a ZIP file, with incrementing name

import zipfile
import os


def backupToZip(folder):
    # backup contents of folder to ZIP file

    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

# create the ZIP file
    print('creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

# walk the directory and compress files in each folder
    for dirname, subdirs, files in os.walk(folder):
        print('Adding files in %s...' % (dirname))
        backupZip.write(dirname)  # add current folder
        for file in files:  # add files in folder to ZIP
            newBase = os.path.basename(dirname) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue  # don't back up ZIP file
            backupZip.write(os.path.join(dirname, file))
    backupZip.close()
    print('Done.')


backupToZip("./")
