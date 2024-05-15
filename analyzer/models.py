from django.db import models
from django.urls import reverse
from accounts.models import User

# Create your models here.
class AudioData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="audios")
    audio = models.FileField(upload_to="audios/")
    prompt = models.CharField(max_length=255, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("audio-detail", kwargs={"pk": self.pk})
    