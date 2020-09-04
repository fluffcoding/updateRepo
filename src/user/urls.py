from django.urls import path
from .views import profile_create, login, register

app_name = 'user'

urlpatterns = [
    path('profile_create/', profile_create, name='profile_create'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]