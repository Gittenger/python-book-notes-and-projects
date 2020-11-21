#! /usr/bin/python3

# launch map in browser using address from CLI

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)
