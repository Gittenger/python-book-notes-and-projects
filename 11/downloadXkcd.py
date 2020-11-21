#! /usr/bin/python3

# downloadXkcd.py - downloads all xkcd comics from home page to hard drive

import requests
import bs4
import os

url = 'http://www.xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # Download the page
    print('Downloading page... %s' % (url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find URL of comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download image
        print('Downloading image... %s' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    # Save image to dir
        imageFile = open(os.path.join(
            'xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get prev button URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://www.xkcd.com' + prevLink.get('href')

print('Done.')
