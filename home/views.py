from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def webmanifest(request):
    return render(request, 'home/site.webmanifest')