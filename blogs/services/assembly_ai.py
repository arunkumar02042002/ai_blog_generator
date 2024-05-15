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
        
    def get_audio_smmary(self, audio_path:str, prompt:str=None) -> str:

        if not prompt:
            prompt = 'Provide a brief summary of the transcript.'
            transcript = self.transcriber.transcribe(audio_path)
            text = transcript.text
        
        try:
            result = transcript.lemur.task(prompt)
            return True, result.response
        
        except Exception as e:
            print(e)
            return False, text
    
assembly = AssemblyAIUtility()