from django.shortcuts import render


def profile_create(request):
    return render(request, 'user/profile_create.html', {})


def login(request):
    return render(request, 'user/login.html', {})


def register(request):
    return render(request, 'user/register.html', {})

    
