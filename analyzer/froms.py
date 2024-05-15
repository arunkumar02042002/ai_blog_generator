from django import forms
from .models import AudioData

class AudioUploadForm(forms.ModelForm):
    
    class Meta:
        model = AudioData
        fields = ['audio','prompt']

    def clean_audio(self):
        audio = self.cleaned_data.get('audio')

        # Check the file extension
        if not audio.name.endswith('.mp3'):
            raise forms.ValidationError("Only MP3 files are allowed.")

        # Check the file MIME type
        if audio.content_type != 'audio/mpeg':
            raise forms.ValidationError("Only MP3 files are allowed.")

        return audio