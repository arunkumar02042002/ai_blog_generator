from pytube import YouTube
from django.conf import settings

import os
import shortuuid

class YouTubeUtility:

    @staticmethod
    def download_audio(youtube_video_link:str) -> bool:
        try:
            selected_video = YouTube(youtube_video_link)
            output_path = settings.MEDIA_ROOT

            audio = selected_video.streams.filter(only_audio=True, file_extension='mp4').first()
            output = audio.download(output_path)

            name, extension = os.path.splitext(output)
            new_name = name+shortuuid.uuid()+'.mp3'
            os.rename(output, new_name)
            print(new_name)
            return {
                'title':selected_video.title,
                'audio_name':new_name.split('/')[-1],
                'audio_path':new_name
            }
        except Exception as e:
            print(e)
            return False