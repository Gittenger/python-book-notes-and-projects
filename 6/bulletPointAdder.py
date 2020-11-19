#! /usr/bin/python3

# bulletPointAdder.py - Adds a bullet point to the start
# of each line of text on the clipboard.

import pyperclip

'''test text
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
'''

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)

'''
test paste here

'''
