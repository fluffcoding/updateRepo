from django.urls import path
from .views import (test_view,
    campaign_list,
    profile_create,
    influencers_assignment,
    campaign_detail,
    memer_assignment, 
    memer_detail,
    memer_dashboard,
    influencer_dashboard,
    login_view,
    register_view,
)

app_name = 'influencer'

urlpatterns = [
    path('test/', test_view, name='create-campaign'),
    path('list/', campaign_list, name='campaign-list'),
    path('profile/', profile_create, name='create-profile'),
    path('task_list/', influencers_assignment, name='assignments-list'), 
    path('detail/', campaign_detail, name='campaign-detail'),
    path('memer/', memer_assignment, name='memer-list'),
    path('memer/detail', memer_detail, name='memer-detail'),
    path('memer_dashboard/', memer_dashboard, name="memer-dashboard"),
    path('influencer_dashboard/', influencer_dashboard, name="influencer-dashboard"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]