import os
from lib.VideoGetter import videoGetter
from lib.VideoSplitter import videoSplitter
from lib.VideoPoster import VideoTweet
	
'''
Does the entire process of getting a video from youtube,
splitting it and posting it to twitter.
'''

if __name__ == "__main__":
  while (True):
    user_input = input("Write a YouTube video URL:\n")
    fragment_length = input("Write a split length:\n")
    video_name = videoGetter(user_input)
    if video_name == 1:
      print("Error downloading video!")
      pass
    else:
      try:
        filename_list = videoSplitter(video_name, int(fragment_length))
        videoTweet = VideoTweet(filename_list[1])
        videoTweet.upload_init()
        videoTweet.upload_append()
        videoTweet.upload_finalize()
        videoTweet.tweet()
        print("Done!\n")
        print("Now deleting video files...\n")
        os.remove(video_name)
        print(video_name, "deleted.")
        for i in filename_list:
          os.remove(i)
          print(i, "deleted.")
        print("All video files deleted.\n")
      except:
        videoTweet = VideoTweet(video_name)
        videoTweet.upload_init()
        videoTweet.upload_append()
        videoTweet.upload_finalize()
        videoTweet.tweet()
        print("Done!\n")
        print("Deleting video file...\n")
        os.remove(video_name)
        print(video_name, "deleted.\n")