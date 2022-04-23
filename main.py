import os
from vimeo_downloader import Vimeo
from countries import links, countries
import random


#loop through big list

for country in countries:
    os.mkdir(rf'D:\travelling channel\{country}')

x = 0
for lst in links:
    random.shuffle(lst)
    c = 0
    country = countries[x]
    x += 1
    for link in lst:
        c += 1
        link = link.replace("external","video")
        link = link.split(".sd", 1)[0] 

        v = Vimeo(link)
        stream = v.streams #>>>[Stream(360p), Stream(540p), Stream(720p), Stream(1080p)]
        stream[-1].download(download_directory= rf"D:\travelling channel\{country}", filename= f'{country}{c}.mp4')
    #store it
    
