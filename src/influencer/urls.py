from django.urls import path
from .views import profile, task_list, dashboard

app_name = 'influencer'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('task_list/', task_list, name='task_list'),
    path('dashboard/', dashboard, name='dashboard'),
]