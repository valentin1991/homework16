from django.shortcuts import render
from . import views


def home (request):
    data = {
    'title':'Главная страница сайта'
    }
    return render(request, 'main/home.html', data )

def servis (request):
    return render (request, 'main/servis.html')

    
