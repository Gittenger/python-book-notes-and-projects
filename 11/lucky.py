#! /usr/bin/python3

# lucky.py - imports several google search results and
# opens them in browser tabs

import requests
import sys
import webbrowser
import bs4

print('Googling...')
res = requests.get('http://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

resultsFile = open('results.html', 'wb')
for chunk in res.iter_content(100000):
    resultsFile.write(chunk)
resultsFile.close()

# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features='lxml')
linkElems = soup.select('#main > div > div > div > a')

# open browser tab for each result
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
