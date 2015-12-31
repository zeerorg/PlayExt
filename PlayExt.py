#!/usr/bin/env python
from selenium import webdriver           # selenium is for basic usage
from bs4 import BeautifulSoup as BS      # for extracting playlist

import time
import wget                   # Downloading
import urllib

import sys
import os

def get_playlist(url):
    pass


def get_download(link):
    pass

if sys.argv[1] == "p":
    get_playlist(sys.argv[2])

elif "youtube" in sys.argv[1]:
    for x in sys.argv[1:]:
        try:
            get_download(x)
        except:
            print("You gave in a wrong argument")
    
else:
    print("WRONG ARGUMENT!!")
    print("Usage: 1. For downloading a single file put one link")
    print("       2. For downloading playlist put 'p <link>'")

    
