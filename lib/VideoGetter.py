from pytube import YouTube, Search, Playlist
from random import randint

'''
Gets a random k-pop video from YouTube. (Currently it extracts it from a playlist)
'''

def randomUrl():
    # n = randint(0, 16)
    # result = Search('kpop').results[n].watch_url
    # return result
    p = Playlist("https://www.youtube.com/playlist?list=PLOHoVaTp8R7dfrJW5pumS0iD_dhlXKv17")
    n = randint(0, len(p.video_urls)-1)
    result = p.video_urls[n]
    return result

def videoGetter(ytURL):
    try:
        myVideo = YouTube(str(ytURL))
    except Exception as e:
        print(e)
        print("Hubo un error con la URL de YouTube")
        return 1
    myVideoStreams = myVideo.streams
    myFilteredStreams = myVideoStreams.filter(file_extension="mp4")
    myFilteredStreams.first().download(filename="input.mp4")
    return "input.mp4"

# if __name__ == "__main__":
#     a = input()
#     videoGetter(str(a))