#!/usr/bin/env python
from selenium import webdriver           # selenium is for basic usage
from bs4 import BeautifulSoup as BS      # for extracting playlist

import time
import wget                   # Downloading
import urllib

import sys
import os

def get_playlist(url):

    source_code = urllib.urlopen(url)
    soup = BS(source_code.read(), "lxml")

    href = []      # contains all links
    title = []     # contains all titles
    dicti = {}     # contains title and corresponding link

    for link in soup.findAll('a', {'class':'pl-video-title-link'}):
        href.append("https://www.youtube.com" + link.get('href'))  # Get link
        title.append(link.string)                                  # Get title
        title[-1] = title[-1][7:-5]
        dicti[title[-1]] = href[-1]

    for x in href:
        get_download(x)        # Send to download


def get_download(link):
    pass

if sys.argv[1] == "p":
    get_playlist(sys.argv[2])

elif "youtube" in sys.argv[1]:
    for x in sys.argv[1:]:
        try:
            get_download(x)
        except:
            print("You gave in a wrong url")
    
else:
    print("WRONG ARGUMENT!!")
    print("Usage: 1. For downloading a single file put one link")
    print("       2. For downloading playlist put 'p <link>'")

    
