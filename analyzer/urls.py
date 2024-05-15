from django.urls import path

from .views import AudioAnalyzerView, AudioDetailView, AudioListView, AudioDeleteView
urlpatterns = [
    path('', view=AudioAnalyzerView.as_view(), name='audio-analyzer'),
    path("audios/", view=AudioListView.as_view(), name="audios"),
    path('audios/<int:pk>/', view=AudioDetailView.as_view(), name='audio-detail'),
    path('audios/<int:pk>/delete/', view=AudioDeleteView.as_view(), name='audio-delete'),
]