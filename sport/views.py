from django.shortcuts import render
from .models import Abonement


# Create your views here.

def index(request):
    all_abonements = Abonement.objects.all()
    context = {
        'abonement': all_abonements,
    }
    return render(request, 'sport/index.html', context)



