from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'contents', 'image']
        #모든 것을 가져올때는 '__all__'로 작성 / 필요한 것만 가져올때는 리스트형태로