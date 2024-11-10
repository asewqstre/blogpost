from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('post-<int:pk>', views.PostsDetailed.as_view(), name="postsDetailed")
]