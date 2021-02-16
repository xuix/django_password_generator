from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html', )


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    # second parameter of get is default
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('+&*%$£!@#~></?'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    password = ''
    for x in range(length):
        password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': password})


def about(request):
    return render(request, 'generator/about.html', )
