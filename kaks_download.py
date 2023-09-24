"""
This script allows you to download a video from a URL using yt_dlp.

Make sure to install yt_dlp using:
pip install yt_dlp
"""

import yt_dlp

#install yt_dlp using pip install yt_dlp

#enter the url of the video you want to download
url = input("Enter the url of the video you want to download: ")

# Set up options for yt_dlp (You can customize these options if needed)
ydl_opts = {}

# Create a yt_dlp instance and download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# Indicate that the download was successful
print("Downloaded Successfully")
