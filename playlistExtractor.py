#import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import os
import time
import wget
import urllib.request

#url = "https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBsINfLVidNVaZ-7_v1NJIo"
def get_playlist():
    url = input("Enter Playlist URL: ")

    source_code = urllib.request.urlopen(url)
    soup = BS(source_code.read(), "lxml")

    href = []
    title = []
    dicti = {}     # for iteration use data.iteritems()
    for link in soup.findAll('a', {'class':'pl-video-title-link'}):
        href.append("https://www.youtube.com" + link.get('href'))
        title.append(link.string)
        title[-1] = title[-1][7:-5]
        dicti[title[-1]] = href[-1]
    return (href, title, dicti)

#\n      # 8 Beg
#\n    # 6 End
def get_download():
    links,titles,both = get_playlist()
    driver = webdriver.Firefox()
    print(str(titles))
    #elem = driver.find_element_by_id("sf_url")

    #links = ['https://www.youtube.com/watch?v=OEqHuTPpAcs']
    download_links = []
    for linkers in links:
        #elem.send_keys(linkers)
        #elem.send_keys(Keys.RETURN)
        driver.get("http://sfrom.net/"+linkers)
        #time.sleep(10)
        soup = BS(driver.page_source, "lxml")  #since I want page to load here it is
        time.sleep(5)
        soup = BS(driver.page_source, "lxml")
        vid_link = soup.findAll('a',{'class':'link'})
        for video_quality in vid_link:
            if video_quality.get('title') == "video format: 360p" and video_quality.get('download')[-4:] == '.mp4':
                download_links.append(video_quality.get('href'))

    driver.close()
    for x in range(len(titles)):
        download(download_links[x], titles[x])

def download(down_link, file_name):
    #filename = wget.download(down_link)
    print("Downloading "+file_name)
    filename = wget.download(down_link)
    #os.rename("videoplayback", file_name+".mp4")


#getting = input("Enter url to download: ")
#download(getting)
#print(get_playlist()[0])

#title="video format: 360p"
print(get_playlist()[2])

#https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBBnHFDEANbv9q8T4CONGZE
