
from .models import Blog
from django.forms import ModelForm

class BlogUpdateForm(ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content')