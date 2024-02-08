from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
]
