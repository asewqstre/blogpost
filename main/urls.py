from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('home/', views.home),
    path('post-<int:pk>', views.PostsDetailed.as_view(), name="postsDetailed"),
    path('post-<int:pk>/delete', views.DeletePost.as_view(), name="deletePost"),
    path('addpost', views.addPost, name="addPost"),
    path('post-<int:pk>/edit', views.EditPost.as_view(), name="editPost")
]