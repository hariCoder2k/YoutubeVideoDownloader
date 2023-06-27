from pytube import YouTube
import pytube
import ssl
import time
from tqdm import tqdm

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


#type your link below
try:
    link = input("Enter youtube video link:")
    path = input("Enter the path to save the video:")
    print("Download starting please wait.....")
    yt = pytube.YouTube(link)
    stream = yt.streams.get_highest_resolution()
    for i in tqdm(stream.download(path),desc="Downloading...",ascii=False,ncols=100):
        time.sleep(0.01)
    print("Download successful")
except:
    print ("An error occurred! Sorry video cannot be downloaded using this software")
