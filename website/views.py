from django.shortcuts import render
import datetime

# Create your views here.
from django.shortcuts import render

def home_page_view(request):
    interestsList = [
            "Modelação e Texturização 3D",
            "Inteligência artificial", "Realidade virtual",
            "Desenvolvimento de videojogos"
        ]
    context = {
        'dateAndHour': datetime.datetime.now(),
        'interests': interestsList,
        'interestsLen': len(interestsList)
    }
    return render(
        request, 'website/home.html', context)

def contacts_page_view(request):
    context = {
        'email': "pedroinacio.info@gmail.com"
    }
    return render(request, 'website/contacts.html', context)

def about_page_view(request):
    context = {
        'nickname': "ShiversDev"
    }
    return render(request, 'website/about.html', context)
