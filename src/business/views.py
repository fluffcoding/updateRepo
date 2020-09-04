from django.shortcuts import render


def dashboard(request):
    return render(request, 'business/dashboard.html', {})


def campaign_create(request):
    return render(request, 'business/campaign_create.html', {})


def campaign_detail(request):
    return render(request, 'business/campaign_detail.html', {})
