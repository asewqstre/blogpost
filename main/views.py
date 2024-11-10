from django.shortcuts import render
from . import models

def home(request):
    posts = models.Posts.objects.all()
    return render(request, 'main/home.html', {'posts':posts})