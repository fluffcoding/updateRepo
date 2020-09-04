from django.shortcuts import render


def task_list(request):
    return render(request, 'memer/list.html', {})


def detail(request):
    return render(request, 'memer/detail.html', {})
    

def dashboard(request):
    return render(request, 'memer/dashboard.html', {})
