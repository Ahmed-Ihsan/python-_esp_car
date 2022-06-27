from pytube import YouTube
url = r"https://www.youtube.com/watch?v=NyLF8nHIquM"
yt = YouTube(url) 
stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
stream.download()