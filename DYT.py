from __future__ import unicode_literals
import youtube_dl


def DownloadVideo(url):
    ydl_opts = {
        'outtmpl': '/home/nomeutente/cartella/YT/Video/%(title)s-%(id)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def DownloadAudio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/home/nomeutente/cartella/YT/Audio/%(title)s-%(id)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    print("vuoi scaricare un video o un audio")
    s = input("> ")
    url = input("inserire link video: ")
    if s == "v":
        DownloadVideo(url)
    elif s == "a":
        DownloadAudio(url)
    else:
        print("errore")


if __name__ == '__main__':
    main()
