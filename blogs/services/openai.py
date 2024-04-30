




from django.conf import settings
from openai import OpenAI

class OpenAIUtility:
    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
    
    def generate_blog(self, transcript):     

        prompt = f"Write a comprehensive blog article based on the transcript extracted from the youtube video.\n\ntranscript: {transcript}\n\nArticle:"


        response = self.client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt
            )
        content = response.choices[0].text.strip()
        return content
    
openai_generator = OpenAIUtility()