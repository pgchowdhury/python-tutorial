"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 21-Nov-2024
    Project: Download YouTube Video
    Library: pytubefix -- pip install pytubefix
"""
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_video(location, url):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        res_streams = yt.streams.get_highest_resolution()
        res_streams.download(output_path=location)
        print("The Video Downloaded Succefully !")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    location = 'automation/videodownloader'
    url = input('Please enter the URL to Dowload Video: ')
    download_video(location, url)
