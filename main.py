import os
from vimeo_downloader import Vimeo
from countries import links, countries


#loop through big list
    #create a folder
for country in countries:
    os.mkdir(rf'D:\travelling channel\{country}')
#loop the nested list
    # download video
for lst in links:
    for link in lst:
        link = link.replace("external","video")
        link = link.split(".sd", 1)[0] 
    #store it
    
