from django.urls import path

from posts import views

app_name = 'posts'
urlpatterns = [
    path('create/', views.post_create, name='create-post'),
    path('my_post/', views.my_posts, name='my-post'),
    path('like/', views.like_post, name='like-post'),
]
