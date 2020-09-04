from django.shortcuts import render


def profile(request):
    return render(request, 'influencer/profile.html', {})


def task_list(request):
    return render(request, 'influencer/assignment_list.html', {})


def dashboard(request):
    return render(request, 'influencer/dashboard.html', {})
