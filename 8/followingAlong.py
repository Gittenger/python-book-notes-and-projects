#! /usr/bin/python3

# following along with examples in book to get comfortable
# using file system commands with python

import os

totalSize = 0
for filename in os.listdir("/home/john/0-cwp"):
    totalSize = totalSize + \
        os.path.getsize(os.path.join("/home/john/0-cwp", filename))

print(totalSize)
