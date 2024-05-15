from .services.assembly_ai import assembly
from .services.youtube import YouTubeUtility
from .services.openai import openai_generator

class BlogGenerator():

    @staticmethod
    def generate(youtube_video_link:str) -> str:

        result = YouTubeUtility.download_audio(youtube_video_link=youtube_video_link)
        if not result:
            raise ValueError("Invalid link!")
        transcript = assembly.get_transcript(result['audio_path'])
        
        if not transcript:
            raise ValueError("Could not generate transcript.")
        
        try:
            content = openai_generator.generate_blog(transcript=transcript)
            return {
                **result,
                "status":True,
                "content":content,
            }
        except:
            return {
                **result,
                "status":False,
                "content":transcript,
            }
