#! /usr/bin/python3

import zipfile
from zipfile import ZipFile
import os

with ZipFile('myZip.zip', 'w') as zipObj:
    for folderName, subfolders, filenames in os.walk("./"):
        zipObj.write(folderName)
        for filename in filenames:
            filePath = os.path.join(folderName, filename)
            zipObj.write(filePath, compress_type=zipfile.ZIP_DEFLATED)
    zipObj.close()
