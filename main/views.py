from django.shortcuts import render, redirect
from . import models
from django.views import generic
from . import forms

def home(request):
    posts = models.Posts.objects.all()
    return render(request, 'main/home.html', {'posts':posts})

class PostsDetailed(generic.DetailView):
    model = models.Posts
    template_name = 'main/postsDetails.html'
    context_object_name = 'post'

class DeletePost(generic.DeleteView):
    model = models.Posts
    template_name = 'main/deletePost.html'
    context_object_name = 'post'
    success_url = '/home/'

def addPost(request):
    if request.method == 'POST':
        form = forms.PostsForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('/home')  
    else:
        form = forms.PostsForm()

    form = forms.PostsForm()
    return render(request, 'main/addPost.html', {'form':form})

class EditPost(generic.UpdateView):
    model = models.Posts
    template_name = 'main/addPost.html'
    context_object_name = 'post'
    success_url = '/home'
    fields = ['title', 'content']