import os
from vimeo_downloader import Vimeo
from countries import links, countries
import random
import moviepy.editor as mp

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
    
for country in countries:
    video = mp.VideoFileClip(rf"D:\travelling channel\{country}\{country}1.mp4")
    country = country.lower()

    logo = (mp.ImageClip(rf"C:\Users\USUARIO\Desktop\channels\travelling channel\overlays\{country}.png")

    .set_start(3)  
    .set_end(video.duration - 2)  
    .set_pos(("center")))

    logo = logo.crossfadein(2.0)
    logo = logo.crossfadeout(2.0)

    final = mp.CompositeVideoClip([video, logo])

    country = country.capitalize()
    final.write_videofile(rf"D:\travelling channel\{country}\{country}1.mp4")
