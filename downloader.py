from pytube import YouTube


link = "https://web.facebook.com/100050302577419/videos/433367175263372/?extid=WA-UNK-UNK-UNK-AN_GK0T-GK1C"

YouTube_1 = YouTube(link)

# print(YouTube_1.title) download vedio title
# print(YouTube_1.thumbnail_url) download vedio thunmnail

# print(YouTube_1.thumbnail_url)

videos = YouTube_1.streams.all() #All format

videos = YouTube_1.streams.filter(only_audio=True) #only for audio downlaod

vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("enter : "))
videos[strm].download()

print("Successfully")

#for downloading whole playlist from youtube

# from pytube import Playlist

# py = Playlist(" Enter your playlist url ")

# print(f"Downloading : {py.title}")

# for video in py.videos:
#     video.streams.first().download()