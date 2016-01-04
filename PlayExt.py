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

    for x in title:
        get_download(dicti[x], x)        # Send to download


def get_download(link, title=None):
    driver = webdriver.Firefox()
    driver.get("http://sfrom.net/"+link)
    soup = BS(driver.page_source, "lxml")# since I want page to load here it is
    time.sleep(10)                       # wait time for download to calculate
    soup = BS(driver.page_source, "lxml")  # scrap page again after waiting
    
    vid_link = soup.findAll('a',{'class':'link'})
    download_link = ""

    # To get 360p link
    for video_quality in vid_link:
        if video_quality.get('title') == "video format: 360p" and\
           video_quality.get('download')[-4:] == '.mp4':
            download_link = video_quality.get('href')

    driver.close()
    
    filename = wget.download(download_link)  # Download File

        
def start():
    if sys.argv[1] == "p":
        get_playlist(sys.argv[2])

    elif "youtube" in sys.argv[1]:
        for x in sys.argv[1:]:
        #try:
            get_download(x)
        #except:
        #    print("You gave in a wrong url")
    
    else:
        print("WRONG ARGUMENT!!")
        print("Usage: 1. For downloading a single file put one link")
        print("       2. For downloading playlist put 'p <link>'")

    
if __name__=="__main__":
    start()
