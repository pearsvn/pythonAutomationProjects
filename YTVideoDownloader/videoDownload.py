from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
folder = 'ENTER THE PATH TO THE FOLDER WHERE YOU WANT TO SAVE THE VIDEO HERE'
stream.download(folder)

"""
    When you run the script in the terminal, you need to pass the link of the video as an argument.
    For example:
        python videoDownload.py https://www.youtube.com/watch?v=ZbZSe6N_BXs
"""