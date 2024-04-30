import assemblyai as aai
from django.conf import settings


class AssemblyAIUtility:

    def __init__(self) -> None:
        aai.settings.api_key = settings.ASSEMBLYAI_API_KEY
        self.transcriber = aai.Transcriber()

    def get_transcript(self, audio_path:str) -> str:
        try:
            transcript = self.transcriber.transcribe(audio_path)
            return transcript.text
        except Exception as e:
            return False
    
assembly = AssemblyAIUtility()