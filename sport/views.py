from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'sport/index.html')

def sport(request):
    return render(request, 'sport/index.html')