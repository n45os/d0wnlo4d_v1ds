import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
import os
from clint.textui import progress
from dataclasses import dataclass
from typing import List
from typing import NamedTuple
import random
import string
import sys

#GLOBALS
after_video = 0 #if something goes wrong, start again after a cerain vid
download_path = "ENTER_YOUR_PATH_HERE" # for example, /Volumes/my_harddrive/my_file





def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@dataclass
class Site:
    url : str = ''
    vid_links : str = ''
    vid_names : str = ''
    name : str = "download"



def get_video_name(sites):
    check_for_titles = sites.copy()
    print("getting the video title")
    for site in check_for_titles:
        r = requests.get(site.url)
        soup = BeautifulSoup(r.content, "lxml")
        for link in soup.title:
            site.vid_links.append(soup.title.string)
    return sites 



def get_all_mp4_links_from(sites):
    print("links collected. extracting files...")
    for site in sites:
        r = requests.get(site.url)
        soup = BeautifulSoup(r.content, "lxml")
        for link in soup.find_all(  src = re.compile(".mp4"), ):
            site.vid_links.append(link.get("src"))
    return sites 

#print(len(get_all_mp4_links_from("https://www.erome.com/a/Aat3CYQK")))


def download_multiple(sites):
    for site in sites :
        download(site.vid_links , site.name)



def download(links, name):
    downloaded_links = []
    for link in links:
        try:
            code = urlparse(link)[2].split('/')[3].split('.')[0].split('_')[0]
        except:
            code = link[-8:]
        
        if code not in downloaded_links:
            print("tries to get request...")
            #r = requests.get(link , stream = True)
            #print("got the request")
            #print(r.headers)
            print("makes new directory...")
            try :
                os.mkdir("/Volumes/My Passport/MEGA DLs/{}".format(name))
            except OSError:
                print ("Creation of the directory %s failed or already exists" % name)
            if(len(downloaded_links) > after_video - 1):
                with open ("{}/{}/vid.{}.mp4".format(download_path, name, code), "wb") as f:
                    print ("Downloading vid #{} with name {}".format(len(downloaded_links), code))
                    r = requests.get(link, stream=True)
                    total_length = r.headers.get('content-length')

                    if total_length is None: # no content length header
                        f.write(r.content)
                    else:
                        dl = 0
                        total_length = int(total_length)
                        total_length_in_mB = total_length/1000000
                        for data in r.iter_content(chunk_size=4096):
                            dl += len(data)
                            f.write(data)
                            done = int(50 * dl / total_length)
                            sys.stdout.write("\r[{}{}] {}MB/{}MB down".format('=' * done, ' ' * (50-done), round(dl/1000000,3) , round(total_length_in_mB,3)))
                            sys.stdout.flush()

                    #f.write(r.content)
            print("done downloading vid{}".format(code))
            downloaded_links.append(code)
    print("done downloading {}".format(name))

 

def downloadFromCommandLine():
    if download_path == "ENTER_YOUR_PATH_HERE":
        print("YOU HAVE TO ENTER YOUR HARDDRIVE PATH TO CONTINUE. READ THE \"README\" FILE")
        return
    sites = [Site()]
    print("type the urls u wanna download. press x when done")
    x = 0
    i = 0
    while True:
        x = str(input("give the url. type \"x\" if u dont wanna add more: "))
        if x == "x": break
        sites.append(Site())
        sites[i].vid_links = []
        sites[i].vid_names = []
        sites[i].url = x
        name = str(input("type the name or press enter: "))
        if  name != '':
            sites[i].name = name
        else :
            sites[i].name = "download_" + str(i+1) + randomString(4)
        i += 1
    sites.pop()
    get_all_mp4_links_from(sites)
    download_multiple(sites)
    print("ALL DONE")

downloadFromCommandLine()
