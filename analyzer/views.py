from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import ListView, DetailView, DeleteView

from .froms import AudioUploadForm
from .models import AudioData

from blogs.services.assembly_ai import assembly

import os


# Create your views here.
class AudioAnalyzerView(LoginRequiredMixin, View, TemplateResponseMixin):
    from_class = AudioUploadForm
    template_name = 'analyzer/analyze_audio.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'form':self.from_class})

    def post(self, request, *args, **kwargs):
        form = self.from_class(data=request.POST, files=request.FILES)
        if form.is_valid() is False:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
        
        audio_data = form.save(commit=False)
        audio_data.user = request.user
        audio_data.save()

        audio_path = os.path.join(settings.MEDIA_ROOT, audio_data.audio.path)
        status, summary = assembly.get_audio_smmary(audio_path=audio_path, prompt=audio_data.prompt)
        print(status, summary)
        audio_data.summary = summary
        audio_data.save()

        if status:
            response_data = {
                    'success': True,
                    'summary': summary,
                    'audio_data': {
                        'id': audio_data.id,
                        'user': audio_data.user.username,
                        'audio': audio_data.audio.url,
                        'prompt': audio_data.prompt,
                        'summary': audio_data.summary,
                    }
                }
            return JsonResponse(response_data, status=200)
        
        return JsonResponse({'success': False, 'summary':summary, 'errors': "Your account has insufficient funds. Please top up to continue using the API"}, status=500)
    
class AudioListView(LoginRequiredMixin, ListView):
    template_name = 'analyzer/audio_list.html'
    context_object_name = 'audios'

    def get_queryset(self):
        return AudioData.objects.filter(user=self.request.user)


class AudioDetailView(LoginRequiredMixin, DetailView):
    template_name = 'analyzer/audio_detail.html'
    context_object_name = "audio"
    pk_url_kwarg = 'pk'
    
    def get_queryset(self):
        return AudioData.objects.filter(user=self.request.user)

    
class AudioDeleteView(LoginRequiredMixin, DeleteView):
    model = AudioData
    template_name = 'analyzer/audio_delete.html'
    success_url = reverse_lazy('audios')
    context_object_name='audio'