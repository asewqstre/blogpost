from django import forms
from . import models

class PostsForm(forms.ModelForm):
    
    class Meta:
        model = models.Posts
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class':'title','placeholder':'Введите название'}),
            'content':forms.Textarea(attrs={'class':'content','placeholder':'Введите содержание статьи'})
            }