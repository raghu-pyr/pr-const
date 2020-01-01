from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def work(request):
    return render(request, 'work.html')


def service(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
