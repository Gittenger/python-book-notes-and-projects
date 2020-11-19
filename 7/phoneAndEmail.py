#! /usr/bin/python3

# Regex program to find phone numbers and email addresses on clipboard

import pyperclip
import re

# phone regex
phoneRegex = re.compile(r'''(
   (\d{3}|\(\d{3}\))?               # area code
   (\s|-|\.)?                       # separator
   (\d{3})                          # first 3 digits
   (\s|-|\.)?                       # separator
   (\d{4})                          # last four digits
   (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension
)''',
                        re.VERBOSE
                        )

# email regex
emailRegex = re.compile(r'''(
   [a-zA-Z0-9._%+-]+                # username
   @                                # @ symbol
   [a-zA-Z0-9-.]+                   # domain name
   (\.[a-zA-Z]{2,4})                # dot-something
)''', re.VERBOSE)

# find all matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')

'''
Test text...
Here is a bunch of text. 
800-420-7240 There will be phone numbers throughout. 415-863-9900 
415-863-9950 When copied and this program run,
 info@nostarch.com  a list will print and be copied to clipboard
 media@nostarch.com The list will contain emails and phone numbers!
 academic@nostarch.com But! It shouldn't contain anything else 
 help@nostarch.com Try it out to see. 
'''
