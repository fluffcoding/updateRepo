from django.shortcuts import render


def test_view(request):
    return render(request, 'business/campaign_create.html', {})


def campaign_list(request):
    return render(request, 'business/campaign_list.html', {})


def profile_create(request):
    return render(request, 'user/profile_create.html', {})


def influencers_assignment(request):
    return render(request, 'influencer/assignment_list.html', {})


def campaign_detail(request):
    return render(request, 'business/campaign_detail.html', {})


def memer_assignment(request):
    return render(request, 'memer/list.html', {})


def memer_detail(request):
    return render(request, 'memer/detail.html', {})
    

def memer_dashboard(request):
    return render(request, 'memer/dashboard.html', {})


def influencer_dashboard(request):
    return render(request, 'influencer/dashboard.html', {})


def login_view(request):
    return render(request, 'user/login.html', {})


def register_view(request):
    return render(request, 'user/register.html', {})

    