from django.shortcuts import render
from . import models
from django.views import generic

def home(request):
    posts = models.Posts.objects.all()
    return render(request, 'main/home.html', {'posts':posts})

class PostsDetailed(generic.DetailView):
    model = models.Posts
    template_name = 'main/postsDetails.html'
    context_object_name = 'post'